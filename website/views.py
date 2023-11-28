#----------<VIEWS.PY>------------------------------------------------------------------------------------#

#----------<IMPORTS>------------------------------------------------------------------------------------#
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import  login_required, current_user
from .models import Note, User, Portfolio,Admin,Ledger 
from . import db
import json
from datetime import datetime, timedelta
from . import process as p
#
# ----------------------------------------------------------------------------------------------#
# BLUEPRINT:create instance of the instance path blueprint
views = Blueprint("views", __name__)
public = Blueprint("public", __name__, template_folder="/public/")

# ----------------<Vars/Lists>------------------------------------------------------------------------------#
FREQUENCY_TO_DAYS = {
    'single': 1,       # Single entry, no conversion needed
    'daily': 1,        # Daily, already per day
    'weekly': 7,       # Weekly
    'bi-weekly': 14,   # Bi-weekly
    'monthly': 30,     # Approximation
    'quarterly': 91,   # Approximation
    'yearly': 365      # Common year
}

# ----------<LANDING_PAGES>------------------------------------------------------------------------------------#
# # HOME
@views.route("/home/", methods=["GET", "POST"])
@login_required
def home():
    range_days = request.args.get('range', default='30')  # Default to 30 days
    start_date = datetime.today()
    end_date= start_date  + timedelta(days=int(range_days))
    session = db.session
    ledger = Ledger
    p.printProccess(start_date,end_date)
    # Format dates into strings in the 'DD/MM/YYYY' format
    start_date_str = start_date.strftime(f'%Y/%m/%d')
    end_date_str = end_date.strftime(f'%Y/%m/%d')
    # Query for the user's ledgers
    if request.method == "POST":
        # Update start and end dates based on form input
        start_date_str = request.form.get("start_date")
        end_date_str = request.form.get("end_date")
        try:
            start_date = datetime.strptime(start_date_str, f'%Y/%m/%d')
            end_date = datetime.strptime(end_date_str, f'%Y/%m/%d')
            start_date_str = start_date.strftime(f'%Y/%m/%d')
            end_date_str = end_date.strftime(f'%Y/%m/%d')

            if end_date < start_date:
                flash('End date cannot be before start date.', 'error')
                return redirect(url_for('views.home'))
        except ValueError:
            flash('Invalid date format. Please use DD/MM/YYYY.', 'error')
            return redirect(url_for('views.home'))

    # Fetch and process the data for the chart
    chartData = p.query_and_process_ledger_entries(start_date_str, end_date_str, session, ledger)
    # Calculate ratio
    total = chartData['debit'] + chartData['credit'] + chartData['savings']
    ratio = f"{chartData['debit']/total:.2f}:{chartData['credit']/total:.2f}:{chartData['savings']/total:.2f}" if total > 0 else "N/A"
    p.printProccess(chartData)
    return render_template("home.html", user=current_user, pie_data=chartData, ratio=ratio, range=range_days)

    #return render_template("home.html", user=current_user, pie_data=categorized_totals)
@views.route("/notes/", methods=["GET", "POST"])
@login_required
def notes():
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
            return render_template("notes.html", user=current_user)
    return render_template("notes.html", user=current_user)
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
            Bill =  'Bills'
            Exp = 'Expenses'
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
                        name = data,
                        details = f'My {data} Ledger',
                        user_id = uid
                        )
                    db.session.commit()                    
                    db.session.add(new_portfolio)
                except Exception as e :
                    print("Error creating portfolio")
                    print(e)    
    # Query for the user's ledgers
   # ledgers = Portfolio.query.filter_by(user_id=current_user.id).all()

    # Query for recent activity log (e.g., last 10 ledger entries or edits)
    recent_activities = Ledger.query.filter_by(user_id=current_user.id).order_by(Ledger.timestamp.desc()).limit(10)

    return render_template("portfolio.html", recent_activities=recent_activities,user=current_user)
 
#
#
#LEDGER
@views.route("/ledger/", methods=["GET", "POST"])
@login_required
def ledger():
    default_ledger = 'Expenses'
    name = request.args.get('ledger')
    data = request.args
    ledgers = Ledger.query.all()  # Replace with your actual query
    if request.method == "GET":
        print(data)
        return render_template("ledger.html",default_ledger=name,ledgers=ledgers,user=current_user)
    else:
        return render_template("ledger.html", default_ledger=default_ledger,ledgers=ledgers,user=current_user)
    
# ... other routes ...

@views.route('/delete_ledger_entry/<int:id>', methods=['POST'])
def delete_ledger_entry(id):
    ledger_to_delete = Ledger.query.get_or_404(id)
    db.session.delete(ledger_to_delete)
    db.session.commit()
    return redirect(url_for('views.ledger'))        
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
    print(jsonify({}))

    return jsonify({})




@views.route('/add_ledger_entry', methods=['GET','POST'])
def add_ledger_entry():
    modelClass = request.form.get('class') #select ledger class
    frequency = request.form.get('frequency') #select frequency
    name = request.form.get('name') #name of ledger
    details = request.form.get('description') #description of ledger
    amount = float(request.form.get('amount')) #amount of ledger
    start_date_str = request.form.get('start_date') #start date of ledger
    end_date_str = request.form.get('end_date')    #end date of ledger
    
    

    # Convert the frequency to a daily amount
    if frequency in FREQUENCY_TO_DAYS:
        days = FREQUENCY_TO_DAYS[frequency]
        amount /= days
    else:
        flash('Invalid frequency selected.', 'error')
        return redirect(url_for('views.ledger'))

    # Convert date strings to datetime objects
    try:
        start_date = datetime.strptime(start_date_str, '%d/%m/%Y').date()
        end_date = datetime.strptime(end_date_str, '%d/%m/%Y').date() if end_date_str else None

        # Validate that start date is not in the future and end date is not before start date
        if start_date > datetime.now().date():
            flash('Start date cannot be in the future.', 'error')
            return redirect(url_for('views.ledger'))

        if end_date and end_date < start_date:
            flash('End date cannot be before start date.', 'error')
            return redirect(url_for('views.ledger'))

    except ValueError:
        flash('Invalid date format. Please use DD/MM/YYYY.', 'error')
        return redirect(url_for('views.ledger'))

    apr = 0.0
    uid = current_user.id #get user id to validate database prerequisites
    debt = True
    if name == 'Salary':
        debt = False
    print(f"name: {name}, user_id: {uid}")
    # Find the portfolio with the same name as the name and belongs to the current user
    pid = Portfolio.query.filter_by(name=modelClass, user_id=uid).first()
    print(pid)
    # If no matching portfolio is found, flash an error message and redirect
    if not pid:
        flash('No portfolio found with the given name.', 'error')
        return redirect(url_for('views.ledger'))

    # Create and save the new ledger entry
    new_ledger_entry = Ledger(name=name,
                            debt=debt,
                            amount=amount,
                            freq=frequency,
                            modelClass=modelClass,
                            details=details,
                            begin=start_date,
                            end=end_date,
                            apr=apr,
                            hide=False,
                            port_id=pid.id,
                            user_id=uid)

    db.session.add(new_ledger_entry)
    db.session.commit()
    flash('New ledger entry added successfully!', 'success')
    return redirect(url_for('views.ledger'))

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
# ----------<ADMIN>------------------------------------------------------------------------------------#
#
@views.route("/dashboard_admin/", methods=["GET", "POST"])
@login_required
def dashboard_admin():
    return render_template("dashboard_admin.html", user=current_user)
#
# ----------<END>------------------------------------------------------------------------------------#
@public.route("/test/", methods=["GET", "POST"])
def test():
    data = request.form
    print(data)
    return render_template("test.html", user=current_user)