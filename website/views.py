#----------<VIEWS.PY>------------------------------------------------------------------------------------#
#
#
#
#----------<IMPORTS>------------------------------------------------------------------------------------#
#
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note, User, Portfolio
from . import db
import json
#
# ----------------------------------------------------------------------------------------------#
#
# BLUEPRINT:create instance of the instance path blueprint
views = Blueprint("views", __name__)
public = Blueprint("public", __name__, template_folder="/public/")
#
#
# ----------<LANDING_PAGES>------------------------------------------------------------------------------------#
# # HOME
@views.route("/home/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")  # Gets the note from the HTML

        if len(note) < 1:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(
                data=note, user_id=current_user.id
            )  # providing the schema for the note
            db.session.add(new_note)  # adding the note to the database
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)
#
#
# WELCOME check username and email
@views.route("/", methods=["GET", "POST"])
def welcome():
    userDetails = current_user
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")

        user_e = User.query.filter_by(email=email).first()
        user_u = User.query.filter_by(username=username).first()
        if user_e:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if user_u:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        else:
            flash("Email and username are available.", category="success")
            return render_template("welcome.html", user=current_user)

    flash(f"We hope you choose our app! {userDetails}")
    return render_template("welcome.html", user=current_user)
#
#
# ----------<FUNCTIONS>------------------------------------------------------------------------------------#
#
#
# DELETE_NOTE
@views.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    note = json.loads(
        request.data
    )  # this function expects a JSON from the INDEX.js file
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
#
#
# ----------<PUBLIC_PAGES>------------------------------------------------------------------------------------#
# SUPPORT
@public.route("/support/", methods=["GET", "POST"])
def support():
    return render_template("support.html", user=current_user)
#
#
# ABOUT
@public.route("/about/", methods=["GET", "POST"])
def about():
    data = request.form
    print(data)
    return render_template("about.html", user=current_user)
#
#
# SETTINGS
@views.route("/settings/", methods=["GET", "POST"])
@login_required
def settings():
    return render_template("settings.html", user=current_user)
#
#
# ----------<APP_PAGES>------------------------------------------------------------------------------------#
# PORTFOLIO
@views.route("/portfolio/", methods=["GET", "POST"])
@login_required
def portfolio():
    return render_template("portfolio.html", user=current_user)
#
#
# CALCULATOR
@public.route("/calculator/", methods=["GET", "POST"])
def calculator():
    data = request.form
    print(data)
    return render_template("calculator.html", user=current_user)
#
#
# ----------<ADMIN_PAGES>------------------------------------------------------------------------------------#
#
# DASHBOARD
@views.route("/dashboard_admin/", methods=["GET", "POST"])
@login_required
def dashboardAdmin():
    return render_template("dashboard_admin.html", user=current_user)
#
#
#
#
# ----------<END>------------------------------------------------------------------------------------#
