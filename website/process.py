
#----------<PROCESS.PY>------------------------------------------------------------------------------------#
#----------<IMPORTS>------------------------------------------------------------------------------------#
from .models import  Ledger, Portfolio, User
from flask_login import current_user
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash#, check_password_hash
from colorama import init, Fore, Style, Back
import timeit

# Initialize Colorama
init(autoreset=True)
#----------<FUNCTIONS>------------------------------------------------------------------------------------#
global asciiimage
asciiimage = r'.\website\static\\ascii_art_FAlogo.txt'
FREQUENCY_TO_DAYS = {
    'single': 1,       # Single entry, no conversion needed
    'daily': 1,        # Daily, already per day
    'weekly': 7,       # Weekly
    'bi-weekly': 14,   # Bi-weekly
    'monthly': 30,     # Approximation
    'quarterly': 91,   # Approximation
    'yearly': 365      # Common year
}

# PRINT_PROCESS
def printProccess(*args):
    for arg in args:
        print(Fore.GREEN + 'Process= ' + Fore.CYAN + str(arg))

# PRINT_CRITICAL
def printCritical(*args):
    for arg in args:
        print(Fore.RED + 'Critical= ' + Fore.YELLOW + str(arg))

# PRINT_WARNING
def printWarning(*args):
    for arg in args:
        print(Fore.YELLOW + 'Warning= ' + Fore.LIGHTYELLOW_EX + str(arg))

# PRINT_RETURN
def printReturn(*args, **kwargs):
    print(Fore.GREEN + 'Return= ' + Fore.CYAN+'<' + str(args) + ',' + str(kwargs) + '>')

#SHA256
def sha256(i):
    sha=generate_password_hash(i)
    printProccess('<sha256>')
    short = sha[:10] + '...'
    printReturn(process='sha256',return_value=short)
    return sha

# Default Protfolio
def defaultPorfolio(user):
    from . import db
    
    uid = user.id #get user id to validate database prerequisites
    
    pid = Portfolio.query.filter_by(user_id=uid).first()
    printReturn('<debug>',uid,process='defaultPorfolio',return_value=pid)
 
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
                    printWarning("Error creating portfolio")
                    printWarning(e)                    
                    pass
# Frequency Converter (actual to per Day)
def freqConverter(amount,freq):
        if freq in FREQUENCY_TO_DAYS:
            days = FREQUENCY_TO_DAYS[freq]
            amount /= days
            return amount
# Define a function to generate test accounts


from datetime import datetime

def query_and_process_ledger_entries(start_date, end_date, session, Ledger):
    """
    Query the Ledger table and process entries for the current user within a given date range.

    Args:
    start_date_str (str): Start date for the range in 'YYYY-MM-DD' format.
    end_date_str (str): End date for the range in 'YYYY-MM-DD' format.
    session: The database session for executing the query.
    Ledger: The SQLAlchemy table object for the ledger.

    Returns:
    dict: A dictionary with categorized totals ('debit', 'credit', 'savings','realized_savings').
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, f'%Y/%m/%d').date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, f'%Y/%m/%d').date()

    # Querying the ledger table for transactions within the date range
    ledger_entries = session.query(Ledger).filter(
        Ledger.end >= start_date,
        Ledger.begin <= end_date,
        Ledger.user_id == current_user.id  # Assuming current_user is defined in your context
    ).all()
    categorized_totals = {'debit': 0, 'credit': 0, 'savings': 0, 'realized_savings': 0}
    
    for entry in ledger_entries:
        overlap_start = max(entry.begin, start_date)
        overlap_end = min(entry.end, end_date)
        num_days = (overlap_end - overlap_start).days + 1
        total_amount = entry.amount * num_days

        if entry.modelClass == 'Savings':
            categorized_totals['realized_savings'] += total_amount
        elif entry.debt:
            categorized_totals['debit'] += total_amount
        else:
            categorized_totals['credit'] += total_amount

    categorized_totals['savings'] = max(categorized_totals['credit'] - categorized_totals['debit'] - categorized_totals['realized_savings'], 0)
    printReturn(process='query_and_process_ledger_entries',return_value=categorized_totals)
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

# Function to print ASCII art from a saved file
def print_ascii_from_file(file_path):
    from colorama import init, Fore, Style
    init(autoreset=True)  # Initializes colorama to wrap stdout/stderr with color codes
    with open(file_path, 'r') as file:
        # Read the contents of the file into a string
        content = file.read()
        # Split the content by newlines to get each line
        lines = content.split("\n")
        for line in lines:
            colored_line = ''
            for char in line:
                if char == '@':
                    colored_line += Fore.BLACK + char
                elif char == '#':
                    colored_line += Fore.YELLOW + char
                elif char == 'S':
                    colored_line += Fore.YELLOW + char
                elif char == '%':
                    colored_line += Fore.BLUE + char
                elif char == '?':
                    colored_line += Fore.BLUE + char
                elif char == '*':
                    colored_line += Fore.CYAN + char
                elif char == '+':
                    colored_line += Fore.WHITE + char
                elif char == ';':
                    colored_line += Fore.LIGHTBLACK_EX + char
                elif char == ':':
                    colored_line += Fore.LIGHTRED_EX + char
                elif char == ',':
                    colored_line += Fore.LIGHTGREEN_EX + char
                elif char == '.':
                    colored_line += Fore.LIGHTYELLOW_EX + char
                # ... add more conditions for other characters and colors if needed
                else:
                    colored_line += char  # Default color
            print(colored_line)

def deleteDB():
    import timeit
    from datetime import datetime
    from . import db
    printProccess('<deleteDB>')
    init(autoreset=True)
    
 
    # ASCII Art Representation of "DELETING DATABASE"
    ascii_art = """
        DDDD   EEEEE L     EEEEE TTTTT I  N  N GGGG
        D   D  E     L     E       T   I  NN  N G   
        D   D  EEEE  L     EEEE    T   I  N N N G  GG
        D   D  E     L     E       T   I  N  NN G   G
        DDDD   EEEEE LLLLL EEEEE   T   I  N   N GGGG 

        DDDD    A   TTTTT  A   BBBB   A   SSSS EEEEE
        D   D  A A    T   A A  B   B A A  S    E    
        D   D AAAAA   T  AAAAA BBBB AAAAA  SSS EEEE 
        D   D A   A   T  A   A B   B A   A    S E   
        DDDD  A   A   T  A   A BBBB  A   A SSSS EEEEE
        """
    sadFace = """
        :(
        """
    def rainbowSadFace():
        print(Fore.MAGENTA + sadFace)
        print(Fore.LIGHTMAGENTA_EX + sadFace)
        print(Fore.LIGHTRED_EX + sadFace)
        print(Fore.LIGHTYELLOW_EX + sadFace)
        print(Fore.LIGHTGREEN_EX + sadFace)
        print(Fore.LIGHTCYAN_EX + sadFace)
        print(Fore.LIGHTBLUE_EX + sadFace)
        print(Fore.LIGHTBLACK_EX + sadFace)
        print(Fore.LIGHTWHITE_EX + sadFace)
        print('...')
        
    # Function to print the ASCII art with specific color
    def print_colored_ascii(ascii_art):
        colored_text = Fore.RED + Back.CYAN + ascii_art + Fore.RESET + Back.RESET
        print(colored_text)
 
        # Function to delete the database and print the ASCII art in color 

    # Function to delete the database and print the ASCII art in color
    def delete():
        def drop_db():
            # This function will contain the code for dropping the database
            db.drop_all()
            db.create_all()  # Recreate the database after dropping

        # Print the colored ASCII art
        print_colored_ascii(ascii_art)

        # Measure the execution time of dropping the database
        start_time = datetime.now()
        execution_time = timeit.timeit(drop_db, number=1)
        end_time = datetime.now()

        # Calculate the time difference
        time_diff = end_time - start_time

        # Return the execution time and the time difference as strings
        return f"Execution time: {execution_time} seconds", f"Time taken: {time_diff}"

    # Execute the function and measure the execution time
    d1 = delete()
    d2 = delete()

    # Assign the execution time to variables
    time1 = d1[0]
    time2 = d2[0]

    timedelete1 = d1[1]
    timedelete2 = d2[1]


    # Print the colored ASCII art
    rainbowSadFace()
    rainbowSadFace()
    # Print the execution time
    printReturn('First',timedelete1,time1) 
    printReturn('Second',timedelete2,time2)
    printCritical('You have deleted the database! -  Please restart the application.')
    

   
def generate_test_accounts():
    
    from . import db
    
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
                amount = freqConverter(random.randint(1, 20), freq)
                portInstance = Portfolio.query.filter_by(name=name,user_id=user.id).first()
                # hashed for debugging
                #print(portInstance.id)
                
                ledger = Ledger(port_id=portInstance.id,
                                user_id=user.id,
                                begin=datetime.now() - timedelta(days=random.randint(1, 365)), 
                                end=datetime.now() + timedelta(days=random.randint(1, 365)),
                                amount=300 if name in ['Salary'] else amount,
                                details=f'{username}: {ledger_name}',
                                apr=5.0 if name in ['Loans'] else 0.0,
                                modelClass = name,
                                name=f'{ledger_name}-{random.randint(1, 100)}',
                                debt=True if name in ['Bills', 'Expenses', 'Loans', 'Subscriptions', 'Savings'] else False,
                                freq=freq)
                db.session.add(ledger)
    # Commit the changes to the database
    db.session.commit()

