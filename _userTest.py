from Python.lib.SetupDB import creator
from Python.lib.ClassManager import Base,User,Ledger,Line
from Python.lib.ConnectionManager import engine
from sqlalchemy.orm import  sessionmaker



creator.createDatabase()

#createDatabase()

def addNow():
    names = ["Anne","Mark","Tina", "Ron", "Clyde","Mary", "Tony","Nina"]
    eml = "@testaccount.net"
    pw = "P@$$w0Rd"
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in names:
        username = f"user{i}"
        email = f"{i}{eml}"
        backupemail = f"{i}backup{eml}"
        password = f"{pw}{i}"
        userAdd = User(username,email,backupemail,password)

        session.add(userAdd)
    session.commit()
    
addNow()  
    