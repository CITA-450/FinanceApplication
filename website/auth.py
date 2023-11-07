# ----------<AUTH.PY>------------------------------------------------------------------------------------#
#
# ----------<IMPORTS>------------------------------------------------------------------------------------#
#
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Admin
from . import db
from flask_login import login_user, login_required, logout_user, current_user
#
# ----------<BUEPRINTS>------------------------------------------------------------------------------------#
#
auth = Blueprint("auth", __name__)  # for authorizing user
#
authAdmin = Blueprint("authAdmin", __name__)  # for authorizing Admin access
#
# ----------<LOGIN/LOGOUT>------------------------------------------------------------------------------------#
#
#
# LOGIN
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                if user.enabled_user == True:
                    return redirect(url_for("views.home"))
                else:
                    return (
                        "<h1>Account Disabled!</h1><h3>*See- violation: policies. </h3>"
                    )
            else:
                flash("WTF!", category="error")
                flash("Incorrect password, use KeePass!", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html", user=current_user)
#
#
# LOGOUT
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
#
#
# ----------<SIGN-UP>------------------------------------------------------------------------------------#
# SIGN_UP
@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        backup_email = request.form.get("backup_email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        elif len(email) < 4:
            flash("Email must be more than 4 characters!", category="error")
        elif email == backup_email:
            flash("backup email is the same as your main email!", category="warning")
        elif len(username) < 2:
            flash("Username must be more than 2 characters!", category="error")
        elif password1 != password2:
            flash("Passwords must match!", category="error")
        elif len(password1) < 7:
            flash("Password must be more than 7 characters!", category="error")
        else:
            new_user = User(
                email=email,
                backup_email=backup_email,
                username=username,
                password=generate_password_hash(password1),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Success!", category="success")
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)
#
#
# ----------<ADMIN_ACCOUNT>------------------------------------------------------------------------------------#
#
#
# ADMIN_ACCOUNT_CREATE
@auth.route("sign_upadmin/", methods=["GET", "POST"])
def createAdmin():
    if request.method == "POST":
        email = request.form.get("email")
        backup_email = request.form.get("backup_email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = Admin.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        elif len(email) < 4:
            flash("Email must be more than 4 characters!", category="error")
        elif email == backup_email:
            flash("backup email is the same as your main email!", category="warning")
        elif password1 != password2:
            flash("Passowrds must match!", category="error")
        elif len(password1) < 7:
            flash("Password must be more than 7 characters!", category="error")
        else:
            new_user = Admin(
                email=email,
                backup_email=backup_email,
                password=generate_password_hash(password1),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Success!", category="success")
            flash("Account created!", category="success")
            return redirect(url_for("views.dashboardAdmin"))

    return render_template("sign_upadmin.html", user=current_user)
#
#
# ADMIN_LOGIN
@auth.route("login_admin/", methods=["GET", "POST"])
def loginAdmin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        admin = Admin.query.filter_by(email=email).first()
        if admin:
            if check_password_hash(admin.password, password):
                flash("Logged in successfully!", category="success")
                login_user(admin, remember=True)
                if admin.enabled_user == True:
                    return redirect(url_for("views.dashboardAdmin"))
                else:
                    return (
                        "<h1>Account Disabled!</h1><h3>*See- violation: policies. </h3>"
                    )
            else:
                flash("WTF!", category="error")
                flash("Incorrect password, use KeePass!", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login_admin.html", user=current_user)
#
#
# ----------<END>------------------------------------------------------------------------------------#
