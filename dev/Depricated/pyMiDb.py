from lib import cnx
import os



#init DB

queryCrt = "CREATE DATABASE if not exists db_cita450;"
queryDB = "SHOW DATABASES"
pathTableUser = f'.\\dotsql\\db_cita450_users.sql'
pathTableLedger = f'.\\dotsql\\db_cita450_ledger.sql'
pathTableLine = f'.\\dotsql\\db_cita450_line.sql'
pathAddTestUser = f".\\dotsql\\test_user.sql"

cnx.connMySQL(queryCrt)
#QryDB = cnx.conn(queryDB)
cnx.connRunSQL(pathTableUser)
cnx.connRunSQL(pathTableLedger)
cnx.connRunSQL(pathTableLine)
cnx.connRunCommitSQL(pathAddTestUser)


#import testcnx

