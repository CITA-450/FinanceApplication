#-- User Class

class User:
    def __init__(self, ID, name, email0, passwd): # Define Self for the User class
        #The DB has the following fields: userID, userName, email, backup email, and password
        self.userID  = ID  #ID
        self.userName = name #name
        self.userEmail_0 = email0 #email
        self.userEmail_1 = None #Backup email
        self.userPass = passwd # Password
# Get Functions
    def details(self): # returns a list or details
        self.attributes = []
        self.attributes = [self.userID,
                           self.userName,
                           self.userEmail_0,
                           self.userEmail_1,
                           self.userPass]
        print(f'User.details> {self.attributes}')
        return (self.attributes)
    def dataSet(self): #return full titled data set on user
        self.details()
        result = {}
        result = {'User_ID':self.attributes[0] ,
                  'Username':self.attributes[1] ,
                  'Email':self.attributes[2],
                  'Backup_Email':self.attributes[3] ,
                  'Password':self.attributes[4] }
        return result
    def getID(self): # return User ID#
        result = self.userID
        return result
    def getUserName(self):# return Username
        result = self.userName
        return result
    def getEmailMain(self):# return User main email
        result = self.userEmail_0
        return result
    def getEmailBackup(self):# return User Backup Email
        result = self.userEmail_1
        return result
    def getUserPassword(self):# return User Password
        result = self.userPass
        return result
    
    
        
        