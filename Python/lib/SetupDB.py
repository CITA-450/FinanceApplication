

from Python.lib.ClassManager import Base,User,Ledger,Line
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
    
    def createDatabase():
        from sqlalchemy import create_engine, text
        
        print("Creating tables")

        Base.metadata.create_all(bind=engine)

    def createTestAccounts():
        from _test_Main_ import session
        from Python.lib.ClassManager import User


          
                
    def createAdminAccount():   
            pass
    def printTest():
            pass    
    """user0 = User(None,f"user{names[0]}",f"{names[0]}{email}",f"{pw}{names[0]}")
        user1 = User(None,f"user{names[1]}",f"{names[1]}{email}",f"{pw}{names[1]}")
        user2 = User(None,f"user{names[2]}",f"{names[2]}{email}",f"{pw}{names[2]}")
        user3 = User(None,f"user{names[3]}",f"{names[3]}{email}",f"{pw}{names[3]}")
        user4 = User(None,f"user{names[4]}",f"{names[4]}{email}",f"{pw}{names[4]}")
        user5 = User(None,f"user{names[5]}",f"{names[5]}{email}",f"{pw}{names[5]}")
        user6 = User(None,f"user{names[6]}",f"{names[6]}{email}",f"{pw}{names[6]}")
        user7 = User(None,f"user{names[7]}",f"{names[7]}{email}",f"{pw}{names[7]}")
        user8 = User(None,f"user{names[8]}",f"{names[8]}{email}",f"{pw}{names[8]}")"""
        
        

        
"""  session.add_all([user0,user1,user2,user3,user4,user5,user6,user7,user8])
        session.commit()"""
        
    
