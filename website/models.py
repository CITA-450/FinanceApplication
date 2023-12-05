#----------<MODELS.PY>------------------------------------------------------------------------------------#



#----------<IMPORTS>------------------------------------------------------------------------------------#


from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#----------<VARS>------------------------------------------------------------------------------------#


#global variables for multipliers
global mult,dayM,weekM,monthM,quartM,yearM,termM
termM = 365.25
day = termM
week = 52.17/termM
month = 12/termM
quarter = 4/termM
half = 2/termM
year = 1/termM
single = 1/termM

#User Classes

#----------<LEDGER>------------------------------------------------------------------------------------#
class currentLedger:
    id:int
    def __init__(self,id):
        id = None
class Ledger(db.Model): #Budget Ledger Lines
    
    mult = single
    
    id= db.Column(db.Integer,primary_key=True)
    timestamp= db.Column(db.DateTime(timezone=True), default=func.now()) #born on date
    name= db.Column(db.String(15),default=None)
    debt= db.Column(db.Boolean,default=True)
    amount= db.Column(db.Float(35),default=0.0)
    modelClass= db.Column(db.String(150),default=None)
    details= db.Column(db.String(150),default='!details')
    begin= db.Column(db.Date,default=func.now())
    end= db.Column(db.Date,default=func.now())
    freq= db.Column(db.String(20))
    apr= db.Column(db.Float(5),default=0.0)
    hide= db.Column(db.Boolean,default=False)
    port_id= db.Column(db.Integer,db.ForeignKey("portfolio.id"))
    user_id= db.Column(db.Integer,db.ForeignKey("user.id"))
    portfolio = db.relationship('Portfolio', back_populates='ledgers')


    def getPerAmount(self): # calculates the amount per actual occurance
        amount = self.amount
        freq = self.freq
        perAmount = amount/freq
        return perAmount
    def getDebtString(self): # Return string value for credit(+) or debit(-)
        debt = self.debt
        d = '-'
        c = '+'
        if debt == True:
            return c
        elif debt == False:
            return d 


#----------<PORTFOLIO>------------------------------------------------------------------------------------#
class Portfolio(db.Model ):
   
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(150))
    enabled= db.Column(db.Boolean,default=True)
    details= db.Column(db.String(150),default='none')
    user_id= db.Column(db.Integer,db.ForeignKey("user.id"))
    ledgers = db.relationship('Ledger', back_populates='portfolio')

#----------<NOTES>------------------------------------------------------------------------------------#
class Note(db.Model ):
    
    id= db.Column(db.Integer,primary_key=True)
    data= db.Column(db.String(10000))
    date= db.Column(db.DateTime(timezone=True),default=func.now())
    user_id= db.Column(db.Integer,db.ForeignKey("user.id"))

#----------<USER>------------------------------------------------------------------------------------#

class User(db.Model,UserMixin):# User class is the main accessor for the user data
    
    id= db.Column(db.Integer,primary_key=True)
    bod= db.Column(db.DateTime(timezone=True), default=func.now()) #born on date
    username= db.Column(db.String(150),unique=True)
    email= db.Column(db.String(150),unique=True)
    backup_email= db.Column(db.String(150))
    password= db.Column(db.String(150),unique=False)
    enabled_user= db.Column(db.Boolean,default=True)
    portfolio= db.relationship("Portfolio")
    notes= db.relationship("Note")
    ledger= db.relationship("Ledger")
    

# Public Classes
#----------<FUNCTIONS>------------------------------------------------------------------------------------#
# # Admin Classes
default_password = 'scrypt:32768:8:1$OLPnOEPh0GATnZts$4b8465926146dcd808bad2e743dc36e63ee8004a7822253af99fe6a167bc240f04e3f0fd6488d1a306d761fc57f021e74f6aea2e013eb1705d36eb3655d888ee'
class Admin(db.Model , UserMixin):

    id= db.Column(db.Integer,primary_key=True)
    bod= db.Column(db.DateTime(timezone=True), default=func.now()) #born on date
    email= db.Column(db.String(150),unique=True)
    backup_email= db.Column(db.String(150),unique=True)
    password= db.Column(db.String(150),default=default_password,unique=False)
    policy= db.Column(db.Integer,default=1)
    enabled_user= db.Column(db.Boolean,default=True)
    