#cnx
 
import mysql.connector
from mysql.connector import errorcode



print("\nLoading-cnx.py...") 
try: #Try to establish a connection
  print("cnx-TRYING...")
  cnx = mysql.connector.connect(user='cita450',
                                password='cita450',
                                database='db_cita450')
  #print result
  print("cnx-ACTIVE...")
  cursor=cnx.cursor()
  print("cnx-TEST-")
  cursor.execute("SHOW TABLES")
  for table in cursor:
    print(table)
  cursor.execute("select * from users as u \
    join ledger as l on l.user_id = u.id \
    join line as n on n.ledger_id = l.id \
    order by l.id;")
  for line in cursor:
    print(line)
  
  
except mysql.connector.Error as err:#error handling
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    print("cnx-INACTIVE")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
    print("cnx-INACTIVE")
  else:
    print(err)
    print("cnx-INACTIVE")
else: #close connection when finished
  print("cnx-KILL...")
  cnx.close()
print("cnx-INACTIVE\n")