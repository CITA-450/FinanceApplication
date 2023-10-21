from lib import cnx

query = "select * from users"
testConn = cnx.conn(query)
print()
print(testConn)