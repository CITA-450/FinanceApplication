from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

DB_NAME = "instance/liteDB_cita450.db"

# Create an engine
engine = create_engine(f"sqlite:///{DB_NAME}")

# Initialize MetaData without the bind parameter
metadata = MetaData()

# Reflect your ledger table
ledger_table = Table('ledger', metadata, autoload_with=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Print column names to test
print(ledger_table.columns.keys())


# futer 
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

def get_financial_data(start_date, end_date):
    # Retrieve data from the database between start_date and end_date
    # This will depend on how your data is stored
    pass

def calculate_totals(data):
    # Calculate the total debit, credit, and savings per day
    # This will depend on the structure of your data
    pass

def calculate_ratio(debit, credit, savings):
    # Calculate the ratio of income:savings:debit
    return credit, savings, debit

def create_pie_chart(debit, credit, savings):
    # Create a pie chart using matplotlib
    fig, ax = plt.subplots()
    ax.pie([debit, credit, savings], labels=['Debit', 'Credit', 'Savings'], colors=['red', 'green', 'blue'], autopct='%1.1f%%')
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    return output.getvalue()

def get_date_range_selection():
    # Get the date range selection from the user
    # This will depend on how you're handling user input
    pass

def create_pdf_report(data):
    # Create a PDF report using a library like reportlab
    # This will depend on the structure of your data and the desired format of the report
    pass