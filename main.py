import tkinter as tk
from tkinter import messagebox

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the username and password are valid
    if username == "admin" and password == "class":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to open the account creation window
def open_create_account_window():
    create_account_window = tk.Toplevel(root)
    create_account_window.title("Create Account")
    
    tk.Label(create_account_window, text="New Username:").pack()
    new_username_entry = tk.Entry(create_account_window)
    new_username_entry.pack()
    
    tk.Label(create_account_window, text="New Password:").pack()
    new_password_entry = tk.Entry(create_account_window, show="*")
    new_password_entry.pack()
    
    create_account_button = tk.Button(create_account_window, text="Create Account", command=create_account)
    create_account_button.pack()

# Function to handle create account button click
def create_account():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()
    
    # Check if the new account details are valid
    if new_username and new_password:
        # add database store logic here
        # show message for debug
        messagebox.showinfo("Create Account", "Account created successfully!")
    else:
        messagebox.showerror("Create Account Failed", "Please provide a username and password.")

# Create the main window
root = tk.Tk()
root.title("Money Buddy")

# Create and configure login page widgets
login_frame = tk.Frame(root)
login_frame.pack(padx=20, pady=20)
tk.Label(login_frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)
tk.Label(login_frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)
login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

# Create and configure create account page widgets
create_account_button = tk.Button(root, text="Create Account", command=open_create_account_window)
create_account_button.pack(padx=20, pady=10)

# Start the main event loop
root.mainloop()