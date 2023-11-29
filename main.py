#----------<MAIN.PY>-------------------------------------------------------------------------------------#
# Import necessary libraries
import socket
from website import create_app
from colorama import init, Fore
from website.process import (printProccess, printCritical, 
                             print_ascii_from_file, asciiimage,printWarning,printReturn,deleteDB,generate_test_accounts)

# Initialize Colorama for colorized terminal output
init(autoreset=True)

# Function to retrieve the current host's IP address
def get_host_ip():
    """Get the current host IP address."""
    try:
        # Connect to an external server to get the public IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()
#----------<TRIGGER>-------------------------------------------------------------------------------------#

# Function to trigger the website launch
def triggerWebsite():
    printProccess("<triggerWebsite>")
    host_ip = get_host_ip()  # Retrieve the host IP address

    # Function to run the app in debug mode on localhost
    def debugLocal():
        printProccess("<trigger> starting on localhost")
        app.run(debug=True, host="localhost", port=5000)

    # Function to run the app in debug mode on host IP
    def debugHost():
        printProccess(f"<trigger> starting on {host_ip}")
        app.run(debug=True, host=host_ip, port=80)

    # Function to host the app on host IP without debug mode
    def host():
        printProccess(f'<trigger> hosting on {host_ip}...')
        app.run(debug=False, host=host_ip, port=80)

    # Prompt user to choose the launch mode 
    #***HIDDEN= local:launch local host , host:host in debug ,test: test mode(db management) , no: exit)
    trigger = input("Do you want to launch your website? Y/n : ")

    if trigger.lower() in ["y", "yes"]:
        # Launch in host mode
        try:
            printProccess(f'Hosting on {host_ip}...')
            print_ascii_from_file(asciiimage)
            host()
        except Exception as err:
            printCritical(f"Error: {err}")
            #triggerWebsite()

    elif trigger.lower() in ["l", "local"]:
        # Launch in local debug mode
        try:
            print_ascii_from_file(asciiimage)
            debugLocal()
        except Exception as err:
            printCritical(f"Error: {err}")
            #triggerWebsite()

    elif trigger.lower() in ["","h", "host"]:
        # Launch in debug mode on host IP
        try:
            print_ascii_from_file(asciiimage)
            debugHost()
        except Exception as err:
            printCritical(f"Error: {err}")
            #triggerWebsite()

    elif trigger.lower() in ["t", "test"]:
        # Launch in test mode
        printWarning("Starting in test mode...")
        # Additional logic for test mode can be implemented here
        print_ascii_from_file(asciiimage)
        trigger = input(Fore.YELLOW+"Do you want to generate test accounts? Y/n")
        if trigger in ["", "y", "Y", "yes", "Yes"]:
            check0 = input(Fore.YELLOW+"Do you want to delete the DB first? Y/n")
            if check0 in ["", "y", "Y", "yes", "Yes"]:
                printCritical(Fore.RED+"this will delete all data"+Fore.YELLOW+" press ENTER to cancel!")
                check1 = input(Fore.YELLOW+'Are you sure? type '+Fore.RED+"'delete'"+Fore.YELLOW+"to confirm: "+Fore.RED)
                if check1 in ["delete", "Delete"]:
                    with app.app_context():
                        # Delete the database
                        deleteDB()
                        # Create the database TEST accounts
                        generate_test_accounts()
                        printProccess("<generate_test_accounts> Complete!")
                        
                elif check1 in ["", "n", "N", "no", "No"]:
                    trigger = input(Fore.YELLOW+"Do you want to generate test accounts? Y/n")
                    if trigger in ["", "y", "Y", "yes", "Yes"]:
                        with app.app_context():
                            generate_test_accounts()
                            printProccess("<generate_test_accounts>", "Complete!")
                    elif trigger in ["n", "N", "no", "No"]:
                        printProccess("<trigger> no...")
                        pass    
        else:
            printWarning("<trigger> no...")
            printProccess('<trigger> starting on '+ Fore.MAGENTA+'localhost(127.0.0.1:5000)...'+Fore.RESET)
            app.run(debug=True, host="localhost", port=5000)
            

    elif trigger.lower() in ["n", "no"]:
        # Exit the program
        printProccess("Exiting...")
        exit()

    else:
        # Handle invalid input
        printProccess('<trigger>',"Invalid input. Exiting...")
        exit()
#----------<RUN>-----------------------------------------------------------------------------------------#

# Main entry point of the script
if __name__ == '__main__':
    # Create an instance of the Flask application
    app = create_app()

    # Trigger the website launch process
    triggerWebsite()
#----------<END>-----------------------------------------------------------------------------------------#
