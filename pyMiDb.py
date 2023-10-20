from lib import cnx
#init DB

queryCrt = "CREATE DATABASE if not exists db_cita450;"
queryDB = "SHOW DATABASES"

Qry1 = cnx.connMySQL(queryCrt)
Qry2 = cnx.conn(queryDB)
print()

print(Qry2)