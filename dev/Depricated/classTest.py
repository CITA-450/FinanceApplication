from xml.etree.ElementTree import tostringlist
from lib.User import User
from lib.Ledger import Ledger
from lib.Line import Line



usr = User(88,'userBob','bos@home.net','pswd')
portLgr = Ledger(990,88,'BobsPersonal','Personal Ledger')
ln = Line(23,990,300.99,1,0,'2023-12-12',None,'classline')


udet = usr.details()
ldet = portLgr.details()
lline = ln.dataSet()

print(lline)
print(usr.dataSet())




