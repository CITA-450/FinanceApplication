from Python.lib.SetupDB import creator
from Python.lib.ClassManager import Base,User,Ledger,Line
from Python.lib.ConnectionManager import engine
from sqlalchemy.orm import Session
from typing import Any,List 


creator.createDatabase()
session = Session(bind=engine)
#createDatabase()
userAdd = User(Username = 'bob', Email ='test', Backup_Email = None, Password = 'sdflhjsdoif')

print(userAdd)
pass
session.add(userAdd)
session.commit()

"""list = []
names = ["Bob","Anne","Mark","Tina", "Ron", "Clyde","Mary", "Tony","nina"]
email = "@testaccount.net"
pw = "P@$$w0Rd"

for name in names:
    
    #print(user)
    print(User)
    list.append(userAdd)
    session.add(userAdd)
    session.commit()
   

#session.add_all(list)"""

        



#session.add_all([user0,user1,user2,user3,user4,user5,user6,user7,user8])
#session.commit()


 
    
    
"""with engine.connect() as connection:
    result = connection.execute()
    
    print(result.all())"""