from Python.lib.ClassManager import User
list = []
names = ["Bob","Anne","Mark","Tina", "Ron", "Clyde","Mary", "Tony","nina"]
email = "@testaccount.net"
pw = "P@$$w0Rd"
        
for name in names:
    try:
        user = User(f"user{name}",f"{name}{email}",f"{pw}{name}")
        #print(user)
        list.append(user)
    except all:
            print('error')

print(list)