from sqlalchemy import create_engine, text
from Python.lib.ClassManager import Base,User,Ledger,Line
print("Main: Importing ConnectionManager")
from Python.lib.ConnectionManager import engine
print('Creating tables')
Base.metadata.create_all(bind=engine)



 
    
    
"""with engine.connect() as connection:
    result = connection.execute()
    
    print(result.all())"""