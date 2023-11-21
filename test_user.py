


from website import create_app
from website.process import generate_test_accounts, printProccess, printReturn


#
#----------<INSTANCE>------------------------------------------------------------------------------------#
#
# start instance

#
#
#----------<TRIGGER>-------------------------------------------------------------------------------------#
#
# TRIGGER

if __name__ == '__main__':
    app = create_app()


    with app.app_context():
        generate_test_accounts()
        printProccess("<generate_test_account()> Complete")
        

#    
#----------<END>-----------------------------------------------------------------------------------------#

