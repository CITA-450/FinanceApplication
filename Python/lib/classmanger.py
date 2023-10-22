# Class Manager
'''This is were all the table magic happens!
The classess assign the attrabute for each table column.
Calling information for an established instance can be done using:
[class].attributes()
[class].dataset()
[class].get%%%%()
or using the connection manager to query the Db'''

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, Mapped


global password
global DataBase 
DataBase = "sqlite:///liteDB_cita450.db"
password = "P@$$w0rD!"

class Base(DeclarativeBase):#Base class the is inherated to the User,Portfolio,Line Classes
    pass

class User(Base):# User base class
    __tablename__ = 'Account'
    ID:Mapped[int]= mapped_column(primary_key = True)
    Username[str] = mapped_column(unique = True,nullable = False)
    Email[str] = (nullable = False)
    Backup_Email[str] = ('Backup_Email',String,default= None)
    Passwd[str] = (nullable = False,default= f'{password}')
    def __init__(self,ID,name,email0,passwd): # Define Self for the User class
        #The DB has the following fields: userID, userName, email, backup email, and password
        self.userID  = ID  #ID
        self.userName = name #name
        self.userEmail_0 = email0 #email
        self.userEmail_1 = None #Backup email
        self.userPass = passwd # Password
# Get Functions
    def details(self): # returns a list or details
        self.attributes = []
        self.attributes = [self.userID,
                           self.userName,
                           self.userEmail_0,
                           self.userEmail_1,
                           self.userPass]
        print(f'User.details> {self.attributes}')
        return (self.attributes)
    def dataSet(self): #return full titled data set on user
        self.details()
        result = {}
        result = {'User_ID':self.attributes[0] ,
                  'Username':self.attributes[1] ,
                  'Email':self.attributes[2],
                  'Backup_Email':self.attributes[3] ,
                  'Password':self.attributes[4] }
        return result
    def getID(self): # return User ID#
        result = self.userID
        return result
    def getUserName(self):# return Username
        result = self.userName
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
class Ledger(Base):# Class Ledger
    __tablename__ = 'Portfolio'
    ID:Mapped[int]= mapped_column('User_ID', primary_key = True)
    userFiD = ('User_ID', String,ForeignKey)
    name = ('Ledger_Name', String)
    dtl = ('Details',String)
    def __init__(self,ID,usrFiD,name,dtl):
        self.ledgerID = ID
        self.userFiD = usrFiD
        self.ledgerName = name
        self.l_details = dtl
    def details(self):
        self.attributes = []
        self.attributes = [self.ledgerID,self.userFiD,self.ledgerName,self.l_details]
        print(f'Ledger.details> {self.attributes}')
        return (self.attributes) 
class Line(Base):# Class Line: the lines populated in the ledger
    __tablename__ = 'Ledger'
    ID:Mapped[int]= mapped_column('User_ID', primary_key = True)
    ldgID = ('Ledger_ID', Integer)
    line_date = ('Line_Date',DATE,)
    amount = ('Amount', float(2))
    deCred = ('Deb_Cred', Boolean, default=True)
    frq = ('Frequency', CHAR,default='S')#may change to 
    dtBgn = ('', Integer)
    dtEnd = ('Date_Begin', DATE, default= None)
    lnDtl = ('Details',String, default= None)

    def __init__(self, ID, ldgID, amnt,deCred,frq,dtBgn,dtEnd,lnDtl): # Define Self for the User class
        #The DB has the following fields: userID, userName, email, backup email, and password
        self.lineID  = ID  #ID
        self.ledger_id = ldgID #ledger_id
        self.line_date = None #line date auto populates
        self.amount = amnt # line Amount decimal(10,2) NOT NULL
        self.deb_cred = deCred # Debit or Credit 0 or 1
        self.freq = frq # Frequency of the occurance using a single CHAR 'S'= single 'W'=week 'B'=bimonth 'M'=month 'H' = Half Year 'Y' = Year 
        self.date_begin = dtBgn # Date that the entry becomes effective
        self.date_end =  dtEnd # Date the entry become ineffective
        self.line_dtl = lnDtl # Details about the line
    #Get Funtions
    def details(self): #return Full list of details
        self.attributes = []
        self.attributes = [self.lineID,
                           self.ledger_id,
                           self.line_date,
                           self.amount,
                           self.deb_cred,
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


engine = create_engine(f'{DataBase}',echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()



