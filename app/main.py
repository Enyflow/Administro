from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
#import matplotlib.pyplot as plt
#import numpy as np
import psycopg2
import psycopg2.extras

url = "host='ec2-54-195-76-73.eu-west-1.compute.amazonaws.com' dbname='d402hlqrc58u86' user='serdtpphaldtog' password='39c8c590bb4387d0c7afbb31793b720131423845898b96ad241434a17ee59b12!'"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/login_',methods=['POST'])
def login_():
     return render_template("login.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
