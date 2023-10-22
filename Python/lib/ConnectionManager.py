#The magic engine that will make all your DB dreams come true


print('ConnectionManager: Starting')
from sqlalchemy import create_engine, text


print('ConnectionManager: Importing Classes')
from Python.lib.ClassManager import DataBase

engine = create_engine(DataBase,echo=True)
print('ConnectionManager: Creating Tables')






"""with engine.connect() as connection:
    result = connection.execute()
    
    print(result.all())"""

