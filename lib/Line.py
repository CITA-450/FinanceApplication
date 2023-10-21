# Line Class


class Line:
    def __init__(self, ID, ldgID, amnt,deCred,frq,dtBgn,dtEnd,lnDtl): # Define Self for the User class
        #The DB has the following fields: userID, userName, email, backup email, and password
        self.lineID  = ID  #ID
        self.ledger_id = ldgID #ledger_id
        self.line_date = None #line date auto populates
        self.amount = amnt # line Amount decimal(10,2) NOT NULL
        self.deb_cred = deCred # Debit or Credit 0 or 1
        self.freq = frq # Frequency of the occurance tinyint NOT NULL
        self.date_begin = dtBgn # Date that the entry becomes effective
        self.date_end =  dtEnd # Date the entry become ineffective
        self.line_dtl = lnDtl # Details about the line



    #Get Funtions
    def details(self): #return Full list of details
        self.attributes = []
        self.attributes = [self.lineID,
                           self.ledger_id,
                           self.line_date,
                           self.amount,
                           self.deb_cred,
                           self.freq,
                           self.date_begin,
                           self.date_end,
                           self.line_dtl]
        print(f'Line.details> {self.attributes}')
        return (self.attributes)

    def dataSet(self):
        self.details()
        result = {}
        result = {'LineID':self.attributes[0],
                  'LedgerID':self.attributes[1],
                  'LineDate':self.attributes[2],
                  'Amount':self.attributes[3],
                  'Deb/Cred':self.attributes[4],
                  'Freqency':self.attributes[5],
                  'Date_Begins':self.attributes[6],
                  'Date_Ends':self.attributes[7],
                  'Line_Details':self.attributes[8]
                  }
        return result
    
    def getLineID(self): # Returns 
        result = self.lineID
        return result
    def getLedgerID(self):# Returns 
        result = self.ledger_id
        return result
    def getLineDate(self):# Returns 
        result = self.ledger_id
        return result
    def getAmount(self):# Returns 
        result = self.amount
        return result
    def getDebCred(self):# Returns 
        result = self.lineID
        return result
    def getFrequency(self):# Returns 
        result = self.lineID
        return result
    def getDateBegin(self):# Returns 
        result = self.lineID
        return result
    def getDateEnd(self):# Returns 
        result = self.lineID
        return result
    def getDetails(self):# Returns 
        result = self.lineID
        return result

        
        
"""  `id` int NOT NULL AUTO_INCREMENT,
  `ledger_id` int NOT NULL,
  `line_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `amount` decimal(10,2) NOT NULL,
  `deb_cred` tinyint(1) DEFAULT NULL,
  `freq` tinyint NOT NULL,
  `date_begin` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `line_dts` varchar(255) NOT NULL,"""       
