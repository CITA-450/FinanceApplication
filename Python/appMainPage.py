#To run click on the url that generates when you run the program

#imports flask using the template main in the templates folder
from flask import Flask, render_template
#from lib import ConnectionManager
#import os to find the templates folder thats in the HTML folder
import os
#Code to find the file path to main.html
app = Flask(__name__, template_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)),'../HTML/templates'))
#used to get the root url
@app.route('/')
#this function will create 'current_amount' and set it to the users amount 
# that is grabbed from the database so it can be used in the main page
def hello_world():
    current_amount = "1,000"  
    return render_template('main.html', current_amount=current_amount)
#runs flask
if __name__ == '__main__':
    app.run()
    