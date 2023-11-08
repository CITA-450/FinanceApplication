# Class Manager
from typing import Any,List 
from sqlalchemy.orm import DeclarativeBase, Mapped ,mapped_column, relationship
from sqlalchemy import orm,create_engine,ForeignKey,text,CHAR,DATE,BOOLEAN,FLOAT

global password
global DataBase 
DataBase = "sqlite:///liteDB_cita450.db"
password = "P@$$w0rD!"
'''This is were all the table magic happens!
The classess assign the attrabute for each table column.
Calling information for an established instance can be done using:
[class].attributes()
[class].dataset()
[class].get%%%%()
or using the connection manager to query the Db'''

class Base(DeclarativeBase):#Base class the is inherated to the User,Portfolio,Line Classes

    pass
    
class User(Base):# User base class
    __tablename__ = 'account'
    UID:Mapped[int]= mapped_column(primary_key = True)
    username:Mapped[str] = mapped_column(unique = True,nullable = False)
    Email:Mapped[str] = mapped_column(nullable = False)
    BackupEmail:Mapped[str]= mapped_column(nullable = True)
    Password:Mapped[str] = mapped_column(nullable = False,default= f'{password}')
    #portfolio:Mapped[List["Ledger"]] = relationship(back_populates = 'account')
    
    
    def __init__(self,username=str,Email=str,BackupEmail=str,Password=str): # Define Self for the User class
        #The DB has the following fields: userID, username, email, backup email, and password
        self.UID  = None  #ID
        self.username = username #username
        self.Email = Email #email
        self.BackupEmail = BackupEmail #Backup email
        self.Password = Password # Password
    def __repr__(self) :#-> str:
        result =  f"({self.UID}) {self.username} ({self.Email},{self.BackupEmail})"
        print(result)
        return result
# Get Functions
    def _details(self): # returns a list or details
        self.attributes = []
        self.attributes = [self.UID,
                           self.username,
                           self.Email,
                           self.BackupEmail,
                           self.Password]
        print(f'User.details> {self.attributes}')
        return (self.attributes)
    def _dataSet(self): #return full titled data set on user
        self.details()
        result = {}
        result = {'User_ID':self.attributes[0] ,
                  'username':self.attributes[1] ,
                  'Email':self.attributes[2],
                  'Backup_Email':self.attributes[3],
                  'Password':self.attributes[4] }
        return result
    def getID(self): # return User ID#
        result = self.userID
        return result
    def getusername(self):# return username
        result = self.username
        return result
    def getEmailMain(self):# return User main email
        result = self.userEmail_0
        return result
    def getEmailBackup(self):# return User Backup Email
        result = self.userEmail_1
        return result
    def getUserPassword(self):# return User Password
        result = self.userPass
        return result

class Ledger(Base):# Class Ledger (Ledger in Portfolio)
    
    __tablename__ = 'portfolio'
    PID:Mapped[int]= mapped_column(primary_key=True)
    UID:Mapped[int] = mapped_column(ForeignKey('account.UID'))
    ledger_Name:Mapped[str] = mapped_column(nullable=False)
    port_details:Mapped[str] = mapped_column('details', default='no details')
    #account:Mapped["User"] = relationship(back_populates='portfolio')
    #lines:Mapped[List["Line"]] = relationship(back_populates = 'portfolio')
    
    def __init__(self,ID,UID,username,details):
        self.ledgerID = ID
        self.account_ID = UID
        self.ledgerName = username
        self.l_details = details
    def details(self):
        self.attributes = []
        self.attributes = [self.ledgerID,self.account_ID,self.ledgerName,self.l_details]
        print(f'Ledger.details> {self.attributes}')
        return (self.attributes)
    def __repr__(self) -> str:
        result =  f"Ledger ID = {self.account_ID},\
            Ledger username = {self.ledgerName}\n\
            Details = {self.l_details}"
        return result 
    
    
class Line(Base):# Class Line(Line in Ledger): the lines populated in the ledger
    
    __tablename__ = 'ledger'
    LID:Mapped[int]= mapped_column(primary_key = True,autoincrement=True)
    PID:Mapped[int] = mapped_column(ForeignKey('portfolio.PID'))
    line_amount:Mapped[float] = mapped_column(nullable=False) 
    deb_Cred:Mapped[bool] = mapped_column(nullable=False,default=True)
    # Frequency Single= 'S',Daily = 'D', Weekly = 'W', Bi-monthly= 'B', monthly = 'M' , Half Year ='H', yearly = 'Y' disable = 'D'
    line_frequency:Mapped[str] = mapped_column(CHAR,nullable=False,default='S')
    datet_Bgn:Mapped[str] = mapped_column(DATE,nullable=False)
    date_End:Mapped[str] = mapped_column(DATE,default= None)
    line_Detail:Mapped[int] = mapped_column(default= None)
    #ledger:Mapped["Ledger"] = relationship(back_populates='ledger')

    def __init__(self,ID,portfolio_ID,amount,debCred,frq,dateBgn,dateEnd,lineDtl): # Define Self for the User class
        #The DB has the following fields: userID, username, email, backup email, and password
        self.lineID  = ID  #ID
        self.ledger_id = portfolio_ID #ledger_id
        self.amount = amount # line Amount decimal(10,2) NOT NULL
        self.debCred = debCred # Debit or Credit 0 or 1
        self.freq = frq # Frequency of the occurance using a single CHAR 'S'= single 'W'=week 'B'=bimonth 'M'=month ,'Q' = quarterly, 'H' = Half Year ,'Y' = Year ,disable = 'D'
        self.date_begin = dateBgn # Date that the entry becomes effective
        self.date_end =  dateEnd # Date the entry become ineffective
        self.line_dtl = lineDtl # Details about the line
    def __repr__(self) -> str:
        result =  f"Line ID = {self.lineID}\n Amount = {self.amount} Credit= {self.debCred} Type = {self.freq}"
        return result 
    #Get Funtions
    def details(self): #return Full list of details
        self.attributes = []
        self.attributes = [self.lineID,
                           self.ledger_id,
                           self.line_date,
                           self.amount,
                           self.debCred,
                           self.freq,
                           self.date_begin,
                           self.date_end,
                           self.line_dtl]
        print(f'Line.details> {self.attributes}')
        return (self.attributes)
    
    def dataSet(self):
        self.details()
        result = {}
        result = {'LineID':self.attributes[0],
                  'LedgerID':self.attributes[1],
                  'LineDate':self.attributes[2],
                  'Amount':self.attributes[3],
                  'Deb/Cred':self.attributes[4],
                  'Freqency':self.attributes[5],
                  'Date_Begins':self.attributes[6],
                  'Date_Ends':self.attributes[7],
                  'Line_Details':self.attributes[8]
                  }
        return result
    
    def getLineID(self): # Returns 
        result = self.lineID
        return result
    def getLedgerID(self):# Returns 
        result = self.ledger_id
        return result
    def getLineDate(self):# Returns 
        result = self.ledger_id
        return result
    def getAmount(self):# Returns 
        result = self.amount
        return result
    def getDebCred(self):# Returns 
        result = self.lineID
        return result
    def getFrequency(self):# Returns 
        result = self.lineID
        return result
    def getDateBegin(self):# Returns 
        result = self.lineID
        return result
    def getDateEnd(self):# Returns 
        result = self.lineID
        return result
    def getDetails(self):# Returns 
        result = self.lineID
        return result





