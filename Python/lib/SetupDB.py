

from Python.lib.ClassManager import Base
print("Main: Importing ConnectionManager")
from Python.lib.ConnectionManager import engine
"""
--To use from main do this:
from Python.lib.SetupDB import creator
creator.createDatabase()
creator.createTestAccounts()
creator.createAdminAccount()
"""

class creator():
    
    def createSessionMaker(commit):
        from Python.lib.ConnectionManager import engine
        from sqlalchemy.orm import  sessionmaker

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(commit)
        session.commit()
        
        

    
    def createDatabase():
        from Python.lib.ClassManager import Base
        from sqlalchemy import create_engine, text
        print("Creating tables")
        Base.metadata.create_all(bind=engine)

    def createTestAccounts():
        from Python.lib.SetupDB import creator
        from Python.lib.ClassManager import User
        creator.createDatabase()
      

        names = ["Anne","Mark","Tina", "Ron", "Clyde","Mary", "Tony","Nina"]
        eml = "@testaccount.net"
        pw = "P@$$w0Rd"
        for i in names:
            username = f"user{i}"
            email = f"{i}{eml}"
            backupemail = f"{i}backup{eml}"
            password = f"{pw}{i}"
            userAdd = User(username,email,backupemail,password)
            creator.createSessionMaker(userAdd)        
    def createAdminAccount():   
            pass
    def printTest():
            pass    