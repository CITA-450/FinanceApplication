#----------<MODELS.PY>------------------------------------------------------------------------------------#



#----------<IMPORTS>------------------------------------------------------------------------------------#


from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#----------<VARS>------------------------------------------------------------------------------------#


#global variables for multipliers
global mult,dayM,weekM,monthM,quartM,yearM,termM
termM = 365.25
dayM = termM
weekM = 52.17857/termM
monthM = 12/termM
quartM = 4/termM
halfM = 2/termM
yearM = 1/termM
sinM = 1/termM

#User Classes

#----------<LEDGER>------------------------------------------------------------------------------------#

class Ledger(db.Model): #Budget Ledger Lines
    
    mult = sinM
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    amount=db.Column(db.Float(35))
    name = db.Column(db.String(150), unique=True)
    details = db.Column(db.String(150))
    begin = db.Column(db.Date, default=func.now())
    end = db.Column(db.Date, default=func.now())
    freq = db.Column(db.String(6), default=mult)
    apr = db.Column(db.Float(5), default = 0.0)
    port_id = db.Column(db.String, db.ForeignKey("portfolio.id"))
    
    def __init__(self, *args, **kwargs):
        pass
    
    def __repr__():
        pass
        
    
    
class Exp(Ledger,db.Model):#Expences and Fees
    mult = weekM
    def __init__(self, *args, **kwargs):
        pass
    def __repr__():
        pass

        
class Bill(Ledger,db.Model):#Bills
    mult = monthM
    def __init__(self, *args, **kwargs):
        pass
    def __repr__():
        pass
    
class Subs(Ledger,db.Model):#Subscriptions
    mult = monthM
    def __init__(self, *args, **kwargs):
        pass
    def __repr__():
        pass

class Tax(Ledger,db.Model):#Taxes 
    mult = yearM
    def __init__(self, *args, **kwargs):
        pass
    def __repr__():
        pass

class Loan(Ledger,db.Model):#Loans
    mult = monthM
    def __init__(self, *args, **kwargs):
        pass
    def __repr__():
        pass

class Sal(Ledger,db.Model):# Salary (default monthly)
    mult = monthM
    def __init__(self, *args, **kwargs):
        pass
    def __repr__():
        pass


class OthInc(Ledger,db.Model):#Other Income
    mult = sinM
    def __init__(self, *args, **kwargs):
        pass
    
    def __repr__():
        pass

#----------<PORTFOLIO>------------------------------------------------------------------------------------#

class Portfolio(db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    ledger_name = db.Column(db.String(150))
    enabled=db.Column(db.Boolean,default=True)
    details = db.Column(db.String(150),default = 'none')
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    portfolio = db.relationship("Ledger")

#----------<NOTES>------------------------------------------------------------------------------------#

class Note(db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#----------<USER>------------------------------------------------------------------------------------#

class User(db.Model , UserMixin):# User class is the main accessor for the user data
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    backup_email = db.Column(db.String(150))
    password = db.Column(db.String(150), unique=False)
    enabled_user = db.Column(db.Boolean, default=True)
    portfolio = db.relationship("Portfolio")
    notes = db.relationship("Note")

# Public Classes
#----------<FUNCTIONS>------------------------------------------------------------------------------------#
# # Admin Classes
default_password = 'scrypt:32768:8:1$OLPnOEPh0GATnZts$4b8465926146dcd808bad2e743dc36e63ee8004a7822253af99fe6a167bc240f04e3f0fd6488d1a306d761fc57f021e74f6aea2e013eb1705d36eb3655d888ee'
class Admin(db.Model , UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    backup_email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150),default=default_password, unique=False)
    policy = db.Column(db.Integer,default=1)
    enabled_user = db.Column(db.Boolean, default=True)
    