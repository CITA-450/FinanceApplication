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

            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
            flash("Email or username already taken.", category="error")
            return render_template("welcome.html", user=current_user)
        else:
            flash("Email must be more than 4 characters!", category="error")
            flash("Email and username are available.", category="success")
            return render_template("welcome.html", user=current_user)

    flash(f"We hope you choose our app! {userDetails}")
    
    return render_template("welcome.html", user=current_user)
#
#
# ----------<APP_PAGES>------------------------------------------------------------------------------------#
# PORTFOLIO
@views.route("/portfolio/", methods=["GET", "POST"])
@login_required
def portfolio():
    uid = current_user.id #get user id to validate database prerequisites
    
    pid = Portfolio.query.filter_by(user_id=uid).first()
    print(f"<User= {uid}>")
    print(f"<Ledgers= {pid}>")
    #if no portfolio ledgers exist, create the default set
    if pid == None:
        if request.method == 'GET':
            Exp = 'Expences'
            Bill =  'Bills'
            Loan = 'Loans'
            Tax = 'Taxes'
            Sub =  'Subscriptions'
            Sal =  'Salary'
            Sav = 'Savings' 
            Othr = 'Other'
            #create list that can be pass into a for loop           
            list = [Exp,Bill,Loan,Tax,Sub,Sal,Sav,Othr]
            #for each list item create a new ledger in portfolio na    
            for data in list:
                try:
                    new_portfolio = Portfolio(
                        ledger_name = data,
                        details = f'My {data} Ledger',
                        user_id = uid
                        )
                    db.session.commit()                    
                    db.session.add(new_portfolio)
                except Exception as e :
                    print("Error creating portfolio")
                    print(e)    
    return render_template("portfolio.html", user=current_user)   
#
#
#LEDGER
@views.route("/ledger/", methods=["GET", "POST"])
@login_required
def ledger():
    data = request.args
    if request.method == "GET":
        print(data)

  
    

        return render_template("ledger.html", user=current_user)
    else:
        return render_template("ledger.html", user=current_user)
        
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


# Open Ledger
@views.route("/open-ledger", methods=["POST"])
@login_required
def open_ledger():
    print('Open Ledger')
    portfolio = json.loads(request.data)
    portfolioId = portfolio["portfolioId"]
    portfolio = Portfolio.query.get(portfolioId)
    print(portfolio)
    if portfolio:
        if portfolio.user_id == current_user.id:
            print(jsonify({}))
            #return redirect(url_for('views.ledger',pid=portfolioId,user=current_user))
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
# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


# Input principal amount, rate, and time from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time period (in years): "))

# Calculate the simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Display the result
print(f"Principal Amount: ${principal}")
print(f"Annual Interest Rate: {rate}%")
print(f"Time Period: {time} years")
print(f"Simple Interest: ${simple_interest:.2f}")
return render_template("calculator.html", user=current_user)

#
#
# ----------<END>------------------------------------------------------------------------------------#
