from flask import Flask, render_template, redirect, request
from datetime import datetime
import csv

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods = ['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            user_data = request.form.to_dict()
            write_data(user_data)
            message = "Your form is submitted. I'll get back to you ASAP"
            return render_template('submit_form.html', message = message)
        except:
            message = "You did't send the message correctly"
            return render_template('submit_form.html', message = message)
    else:
        message = "FORM NOT SUBMITTED"
        return render_template('submit_form.html', message = message)

def write_data(user_data):
    name = user_data['name']
    email = user_data['email']
    message = user_data['message']
    time1 = datetime.now()
    with open('user_records.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter = '|', quotechar = ' ', quoting = csv.QUOTE_MINIMAL)
        db_writer.writerow([name, email, message, time1])
        
if __name__ == "__main__":
    app.run(debug = 'True')
