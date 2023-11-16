#----------<PROCESS.PY>------------------------------------------------------------------------------------#

#----------<IMPORTS>------------------------------------------------------------------------------------#
from werkzeug.security import generate_password_hash, check_password_hash
#----------<FUNCTIONS>------------------------------------------------------------------------------------#

#PRINT_PROCESS
def printProccess(*args):
    
    for arg in args:
        print(f'Process= {arg}')

#PRINT_RETURN
def printReturn(*args, **kwargs):
    print(f'Return= <{args,kwargs}>')
            
#SHA256
def sha256(i):
    sha=generate_password_hash(i)
    printProccess('sha256')
    printReturn(sha,process='sha256')
    return sha

def defaultPorfolio(user):
    pass
    
#----------<TESTMAIN>------------------------------------------------------------------------------------#    
#TEST
if __name__ == '__main__':
    admin = 'admin'
    test = sha256(admin)
    printProccess(test)
#----------<END>------------------------------------------------------------------------------------#