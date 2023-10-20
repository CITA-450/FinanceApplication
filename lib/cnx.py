#cnx
 
import mysql.connector
from mysql.connector import errorcode





def conn(qry):
  _user='cita450'
  _password='cita450'
  _database='db_cita450'
  print("\nLoading-cnx.py...") 
  try: #Try to establish a connection
    print(f"cnx-TRYING...({_database}, with user = {_user})...")
    cnx = mysql.connector.connect(user=_user,password=_password,database=_database)
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
  else:
    #print result
    print("cnx-ACTIVE...")
    cursor=cnx.cursor() #create terminal connection
    result = [] #create list for results
    #send query (qry) then run a for loop to append cursor lines to result[]
    print(f"cnx-EXECUTING... \"{qry}\"")
    cursor.execute(qry)
    print("cnx-APPENDING..")
    for line in cursor: 
      result.append(line)
    print("cnx-KILL...")
    cnx.close()
    print("cnx-INACTIVE")
    print("cnx-RETURN RESULT...")
    print("cnx-EXIT")
    #return result[]
    return result 
  
  
#use for connecting to MySQL prior to DB inti creation

def connMySQL(qry):
  _user='cita450'
  _password='cita450'
  _database='db_cita450'
  print("\nLoading-cnx.py...") 
  try: #Try to establish a connection
    print(f"cnx-TRYING...({qry}, with user = {_user})...")
    cnx = mysql.connector.connect(user=_user,password=_password)
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
  else:
    #print result
    print("cnx-ACTIVE...")
    cursor=cnx.cursor() #create terminal connection
    result = [] #create list for results
    #send query (qry) then run a for loop to append cursor lines to result[]
    print(f"cnx-EXECUTING... \"{qry}\"")
    cursor.execute(qry)
    print("cnx-APPENDING..")
    for line in cursor: 
      result.append(line)
    print("cnx-KILL...")
    cnx.close()
    print("cnx-INACTIVE")
    print("cnx-RETURN RESULT...")
    print("cnx-EXIT")
    #return result[]
    return result 
def runSQL(path):
  import os
  currentDir = os.getcwd()
  _user='cita450'
  _password='cita450'
  _database='db_cita450'
  print("\nLoading-cnx.py...") 
  try: #Try to establish a connection
    print(f"cnx-TRYING...({_database}, with user = {_user})...")
    with open(f'{currentDir}{path}','r') as sql_file:
      sql =sql_file.read()
    cnx = mysql.connector.connect(user=_user,password=_password)
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
  else:
    #print result
    print("cnx-ACTIVE...")
    cursor=cnx.cursor() #create terminal connection
    print(f"cnx-EXECUTING... \"{sql}\"")
    for l in sql:
      try:
        cursor.execute(l)
        print(l)
      except mysql.connector.Error as err:#error handling
        print(err)
    print("cnx-KILL...")
    cnx.close()
    print("cnx-INACTIVE")
    print("cnx-RETURN RESULT...")
    print("cnx-EXIT")
 
   
  
  