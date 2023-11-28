#----------<MAIN.PY>-------------------------------------------------------------------------------------#
#
#----------<IMPORTS>-------------------------------------------------------------------------------------#
from website import create_app, process as P
#
#----------<**SET_IP**>----------------------------------------------------------------------------------#
#
#*CHANGE FOR TO YOUR CURRENT IP ADDRESS(* Set host IP)
ip = "192.168.254.34"
#
#


#
#----------<INSTANCE>------------------------------------------------------------------------------------#
#
# start instance
app = create_app()
#
#
#----------<TRIGGER>-------------------------------------------------------------------------------------#
#
# TRIGGER

if __name__ == '__main__':
    P.printProccess("<trigger>")
    
    trigger = input("Do you want to launch your website? Y/n")
    if trigger == "":
        P.printProccess("debug")
        app.run(debug=True, host="localhost", port=80)
        app.process.generate_test_accounts()
        exit()
    elif trigger == "y" or trigger == "Y":
        P.printProccess(f"hosting on: debug off {ip}")
        app.run(host=ip, port=80)
        exit()
    elif trigger == ("n" or "N"):
        P.printProccess("exiting")
        exit()
    else:
        P.printProccess("trigger error")
        app.aborter()
#   
#    
#----------<END>-----------------------------------------------------------------------------------------#
