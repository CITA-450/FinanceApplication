
#----------<PROCESS.PY>------------------------------------------------------------------------------------#
#----------<IMPORTS>------------------------------------------------------------------------------------#
from .models import  Ledger, Portfolio, User
from datetime import datetime
from werkzeug.security import generate_password_hash#, check_password_hash
#----------<FUNCTIONS>------------------------------------------------------------------------------------#
FREQUENCY_TO_DAYS = {
    'single': 1,       # Single entry, no conversion needed
    'daily': 1,        # Daily, already per day
    'weekly': 7,       # Weekly
    'bi-weekly': 14,   # Bi-weekly
    'monthly': 30,     # Approximation
    'quarterly': 91,   # Approximation
    'yearly': 365      # Common year
}
#PRINT_PROCESS
def printProccess(*args):
    
    for arg in args:
        print(f'Process= {arg}')

#PRINT_RETURN
def printReturn(*args, **kwargs):
    print(f'Return= <{args,kwargs}>')
            
#SHA256
def sha256(i):
    sha=generate_password_hash(i)
    printProccess('sha256')
    printReturn(sha,process='sha256')
    return sha

# Default Protfolio
def defaultPorfolio(user):
    from . import db
    
    uid = user.id #get user id to validate database prerequisites
    
    pid = Portfolio.query.filter_by(user_id=uid).first()
    print(f"<User= {uid}>")
    print(f"<Ledgers= {pid}>")
    #if no portfolio ledgers exist, create the default set
    if pid == None:
       
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
                    
                    pass
# Frequency Converter (actual to per Day)
def freqConverter(amount,freq):
        if freq in FREQUENCY_TO_DAYS:
            days = FREQUENCY_TO_DAYS[freq]
            amount /= days
            return amount
# Define a function to generate test accounts

from flask_login import current_user
from datetime import datetime

def query_and_process_ledger_entries(start_date, end_date, session, Ledger):
    """
    Query the Ledger table and process entries for the current user within a given date range.

    Args:
    start_date (str): Start date for the range in 'YYYY/MM/DD' format.
    end_date (str): End date for the range in 'YYYY/MM/DD' format.
    session: The database session for executing the query.
    Ledger: The SQLAlchemy table object for the ledger.

    Returns:
    dict: A dictionary with categorized totals ('debit', 'credit', 'savings').
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, f'%Y/%m/%d').date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, f'%Y/%m/%d').date()

    # Querying the ledger table for transactions of the current user within the date range
    ledger_entries = session.query(Ledger).filter(
        Ledger.begin <= start_date,
        Ledger.end >= end_date,
        Ledger.user_id == current_user.id  # Filter by current user's ID
    ).all()

    categorized_totals = {'debit': 0, 'savings': 0, 'credit': 0}
    for entry in ledger_entries:
        num_days = (end_date - start_date).days + 1
        total_amount = entry.amount * num_days  # Multiplying the amount by the number of days
        printProccess('query_and_process_ledger_entries')
        printReturn(process='query_and_process_ledger_entries',amount=entry.amount,days=num_days, return_value=total_amount)
        # Categorizing the entries
        if entry.debt:
            categorized_totals['debit'] += total_amount
        else:
            categorized_totals['credit'] += total_amount

    # Calculate 'savings' as credit minus debit
    categorized_totals['savings'] = max(categorized_totals['credit'] - categorized_totals['debit'], 0)

    return categorized_totals
# Note: Ensure this function is called within an application context where `current_user` is available.


# Updated function to calculate daily cumulative amounts with date range filtering
def calculate_daily_cumulative_amounts(transactions, start_date, end_date):
    """
    Calculate the daily cumulative amounts of debits and credits within a given date range.

    Args:
    transactions (list of dicts): List of transaction dictionaries.
                                  Each dictionary should have 'date', 'amount', and varying 'type' keys.
    start_date (str): Start date for the range in 'YYYY-MM-DD' format.
    end_date (str): End date for the range in 'YYYY-MM-DD' format.

    Returns:
    dict: A dictionary with dates as keys and another dictionary as values.
          The inner dictionary has 'debit' and 'credit' as keys with their cumulative amounts.
    """
    printProccess('calculate_daily_cumulative_amounts')
    start_date = datetime.strptime(start_date, f'%Y-%m-%d')
    end_date = datetime.strptime(end_date, f'%Y-%m-%d')

    daily_totals = {}
    for transaction in transactions:
        date = datetime.strptime(transaction['date'], f'%Y-%m-%d')
        amount = transaction['amount']

        # Check if the transaction date is within the specified range
        if start_date <= date <= end_date:
            if date not in daily_totals:
                daily_totals[date] = {'debit': 0, 'credit': 0}

            # Checking for various types and accumulating accordingly
            if 'type' in transaction and transaction['type'] == 'debit':
                daily_totals[date]['debit'] += amount
            elif 'type' in transaction and transaction['type'] == 'credit':
                daily_totals[date]['credit'] += amount
            # Add more conditions as needed for other types
    printReturn(process='calculate_daily_cumulative_amounts',return_value=daily_totals)
    return daily_totals

def generate_test_accounts():
    from . import db
    from datetime import datetime, timedelta
    import random
    # Loop 10 times to create 10 accounts
    for i in range(1, 11):
        # Generate the required data for each account
        username = f'testuser{i}'
        password = sha256('password')
        email = f'{username}@email.com'
        backup_email = f'{username}.backup@email.com'

        # Create a new user and save it to the database
        user = User(email=email,backup_email=backup_email, username=username, password=password)
        db.session.add(user)
        
        # Create user instance
        
        userInstance = User.query.filter_by(email=email).first()
        print(userInstance.id)
        # Create portfolios for the user
        portfolio_names = ['Bills', 'Expenses', 'Loans', 'Taxes', 'Subscriptions', 'Salary', 'Savings', 'Other']
        for name in portfolio_names:
            portfolio = Portfolio(name=name, user_id=userInstance.id)
            db.session.add(portfolio)

            # Create ledgers for the portfolio
            if name == 'Bills':
                ledger_names = ['water', 'gas', 'electric', 'rent', 'internet']
            elif name == 'Expenses':
                ledger_names = ['car', 'phone', 'dentist', 'food', 'clothes', 'restaurant']
            elif name == 'Loans':
                ledger_names = ['loan']
            elif name == 'Subscriptions':
                ledger_names = ['netflix', 'hulu', 'chatGPT']
            elif name == 'Savings':
                ledger_names = ['primary', 'secondary']
            elif name == 'Salary':
                ledger_names = ['My Salary']
            else:
                ledger_names = ['Other']

            for ledger_name in ledger_names:
                freq='monthly' if name in ['Bills', 'Loans', 'Subscriptions', 'Savings', 'Salary'] else 'single'
                amount = freqConverter(random.randint(100, 1000), freq)
                portInstance = Portfolio.query.filter_by(name=name,user_id=user.id).first()
                print(portInstance.id)
                
                ledger = Ledger(port_id=portInstance.id,
                                user_id=user.id,
                                begin=datetime.now() - timedelta(days=random.randint(1, 365)), 
                                end=datetime.now() + timedelta(days=random.randint(1, 365)),
                                amount=amount,
                                details=f'{username}: {ledger_name}',
                                apr=5.0 if name in ['Loans'] else 0.0,
                                modelClass = name,
                                name=f'{ledger_name}-{random.randint(1, 100)}',
                                debt=True if name in ['Bills', 'Expenses', 'Loans', 'Subscriptions', 'Savings'] else False,
                                freq=freq)
                db.session.add(ledger)
    # Commit the changes to the database
    db.session.commit()

