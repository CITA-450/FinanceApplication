#----------<VIEWS.PY>------------------------------------------------------------------------------------#
#
#
#
#----------<IMPORTS>------------------------------------------------------------------------------------#
#
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note, User, Portfolio,Admin,Ledger
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

        user_ee = User.query.filter_by(email=email).first()
        user_eu = User.query.filter_by(email=username).first()
        admin_ea = Admin.query.filter_by(email=email).first()
        admin_ua = Admin.query.filter_by(email=username).first()
        user_be = User.query.filter_by(backup_email=email).first()
        user_bu = User.query.filter_by(backup_email=username).first()
        user_ue = User.query.filter_by(username=email).first()
        user_uu = User.query.filter_by(username=username).first()
        if user_ee:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if user_eu:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if user_be:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if user_bu:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if user_ue:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if user_uu:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if admin_ea:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if admin_ua:
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        if len(email) > 4:
            if len(username) > 2:
                flash(f"-Email-'{email}' -Username-'{username}' Available!", category="success")
                return render_template("sign_up.html", user=current_user)
            else:
                flash("Username must be more than 2 characters!", category="error")
                return render_template("welcome.html", user=current_user)

        else:
            flash("Email must be more than 4 characters!", category="error")
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
    print(jsonify({}))

    return jsonify({})


# Open Ledger
@views.route("/open-ledger", methods=["POST"])
@login_required
def open_ledger():
    print('Open Ledger')
    ledger = json.loads(request.data)
    ledgerID = ledger["ledgerID"]
    ledger = Portfolio.query.get(ledgerID)
    if ledger:
        if portfolio.user_id == current_user.id:
            print("open_ledger user test")
    print(jsonify({}))
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
    this_user = current_user
    uid = this_user.id
    pid = {}
    pid = Portfolio.query.filter_by(user_id=uid).all()
    print(f"<User= {uid}>")
    print(f"<Ledgers= {pid}>")
    if pid == None:
        if request.method == 'GET':
            Exp = 'Expences'
            Bill =  'Bills'
            Loan = 'Loans'
            Tax = 'Taxes'
            Sub =  'Subscriptions'
            Sal =  'Salary'            
            list = [Exp,Bill,Loan,Tax,Sub,Sal]
                
            for data in list:
                try:
                    new_portfolio = Portfolio(
                        ledger_name = data,
                        details = f"My {data}",
                        user_id = this_user.id
                        )
                        
                    db.session.add(new_portfolio)
                    db.session.commit()                    
                except Exception as e :
                    print("Error creating portfolio")
                    print(e)    
    return render_template("portfolio.html", user=current_user)   
#
#
#LEDGER
@views.route("/ledger/", methods=["GET", "POST"])
@login_required
def ledger(ledgerID):
    ledger = ledgerID
    print(f'Access ledger {ledger}')
    
    return render_template("ledger.html", user=current_user, id = ledgerID)
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
# ----------<END>------------------------------------------------------------------------------------#
@public.route("/test/", methods=["GET", "POST"])
def test():
    data = request.form
    print(data)
    return render_template("test.html", user=current_user)