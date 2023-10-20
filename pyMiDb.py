from lib import cnx
import os

os.listdir('FinanceApplication')
#init DB

queryCrt = "CREATE DATABASE if not exists db_cita450;"
queryDB = "SHOW DATABASES"
pathTableUser = f'\\dotsql\\db_cita450_users.sql'
pathTableLedger = f'\\dotsql\\db_cita450_ledger.sql'
pathTableLine = f'\\dotsql\\db_cita450_line.sql'

Qry1 = cnx.connMySQL(queryCrt)
Qry2 = cnx.conn(queryDB)
Qry3 = cnx.runSQL(pathTableUser)
Qry4 = cnx.runSQL(pathTableLedger)
Qry5 = cnx.runSQL(pathTableLine)
print()
print(Qry2)

