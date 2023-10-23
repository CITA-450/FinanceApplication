#Run this to test your account creation on you own machine

from Python.lib.SetupDB import creator as CR
from Python.lib.ClassManager import Base,User,Ledger,Line
from Python.lib.ConnectionManager import engine
from sqlalchemy.orm import  sessionmaker
from typing import Any,List

 
CR.createTestAccounts()