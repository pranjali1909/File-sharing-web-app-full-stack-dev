from flask import Flask,abort,render_template,request
from flask_pymongo import PyMongo
import json
from cfg import config

app = Flask(__name__)
app.config["MONGO_URI"] = config['mongo_uri']
mongo = PyMongo(app)

@app.route('/')
def show_index():
    user_documents = mongo.db.users.find({})
    print(user_documents)

    for doc in user_documents:
        print(doc)
    return 'This is my home page!'


@app.route('/login')
def show_login():
    return render_template('login.html')

@app.route('/check_login',methods=['POST'])
def check_login():
    email = request.form['email5']
    password = request.form['password5']

    print('Email is: '+ email)
    print('Password is:' + password)
    return 'DONE'

@app.route('/signup')
def show_signup():
    return render_template('signup.html')

@app.route('/check_signup',methods=['POST'])
def check_signup():
    emailid = request.form['email4']
    passwordid = request.form['password4']
    

    print('Email is: '+ emailid)
    print('Password is:' + passwordid)
    
    return 'DONE'    
