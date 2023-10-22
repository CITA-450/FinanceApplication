from flask import Flask, render_template
from lib import ConnectionManager


app = Flask(__name__)

@app.route('/')
def hello_world():
    current_amount = "1,000"  
    return render_template('..\\Python\\HTML\\templates\\main.html', current_amount=current_amount)

if __name__ == '__main__':
    app.run()