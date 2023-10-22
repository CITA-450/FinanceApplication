# Class Ledger
from sqlalchemy import create_engine, ForiegnKey, Column, String, Integer, CHAR , DATE, Boolean
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base 



global DataBase 
DataBase = "///liteDB_cita450.db"
Base = declarative_base()

class User(Base):
    __tablename__ = "Accounts"

    ID = Column("User_ID", primary_key = True, unique=True,autoincrement=True)
    name = Column("UserName", String,  )
    Email = Column("Email", String)
    Backup_Email = Column("Backup_Email",String,default= None)
    passwd = Column("Password",String)
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
        print(f"User.details> {self.attributes}")
        result = self.attributes
        return result
    def dataSet(self): #return full titled data set on user
        self.details()
        result = {}
        result = {"User_ID":self.attributes[0] ,
                  "Username":self.attributes[1] ,
                  "Email":self.attributes[2],
                  "Backup_Email":self.attributes[3] ,
                  "Password":self.attributes[4] }
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
class Ledger(Base):
    __tablename__ = "Portfolio"
    ID = Column("ID", primary_key=True, unique=True, autoincrement=True)
    userFiD = Column("User_ID",String,foreign_key=True)
    name = Column("Ledger_Name",String)
    dtl = Column("Details",String)
    def __init__(self,ID,usrFiD,name,dtl):
        self.ledgerID = ID
        self.userFiD = usrFiD
        self.ledgerName = name
        self.l_details = dtl
    def details(self):
        self.attributes = []
        self.attributes = [self.ledgerID,self.userFiD,self.ledgerName,self.l_details]
        print(f"Ledger.details> {self.attributes}")
        return (self.attributes) 
class Line(Base):
    __tablename__ = "Ledger"
    ID = Column("ID", Integer, primary_key=True,  autoincrement=True)
    ldgID = Column("Ledger_ID", Integer, foreign_key=True)
    line_date = Column("Line_Date", DATE)
    amount = Column("Amount", float)
    deCred = Column("Deb_Cred", Boolean, default=True)
    frq = Column("Frequency", CHAR,default="S")#may change to 
    dtBgn = Column("Date_Begin", Integer)
    dtEnd = Column("Date_End", DATE, default= None)
    lnDtl = Column("Details",String, default= None)

    def __init__(self, ID, ldgID, amnt,deCred,frq,dtBgn,dtEnd,lnDtl): # Define Self for the User class
        #The DB has the following fields: userID, userName, email, backup email, and password
        self.lineID  = ID  #ID
        self.ledger_id = ldgID #ledger_id
        self.line_date = None #line date auto populates
        self.amount = amnt # line Amount decimal(10,2) NOT NULL
        self.deb_cred = deCred # Debit or Credit 0 or 1
        self.freq = frq # Frequency of the occurance using a single CHAR "S"= single "W"=week "B"=bimonth "M"=month "H" = Half Year "Y" = Year 
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
        print(f"Line.details> {self.attributes}")
        return (self.attributes)
    def dataSet(self):
        self.details()
        result = {}
        result = {"LineID":self.attributes[0],
                  "LedgerID":self.attributes[1],
                  "LineDate":self.attributes[2],
                  "Amount":self.attributes[3],
                  "Deb/Cred":self.attributes[4],
                  "Freqency":self.attributes[5],
                  "Date_Begins":self.attributes[6],
                  "Date_Ends":self.attributes[7],
                  "Line_Details":self.attributes[8]
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


engine = create_engine(f"sqlite:{DataBase}",echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = User(None,"bill","boss@home.net","p@ssword")



