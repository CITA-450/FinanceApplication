# Class Ledger

class Ledger:
    def __init__(self,ID,usrFiD,name,dtl):
        self.ledgerID = ID
        self.userFiD = usrFiD
        self.ledgerName = name
        self.l_details = dtl
    def details(self):
        self.attributes = []
        self.attributes = [self.ledgerID,self.userFiD,self.ledgerName,self.l_details]
        print(f'Ledger.details> {self.attributes}')
        return (self.attributes) 
            
''' `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `port_dts` varchar(255) DEFAULT NULL,'''