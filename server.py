from flask import Flask,abort,render_template,request,redirect,session
from flask_pymongo import PyMongo
import json
from cfg import config

app = Flask(__name__)
app.config["MONGO_URI"] = config['mongo_uri']
app.secret_key = b'ftcrjcougrufc9fcr/'

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
    email = request.form['email']
    password = request.form['password']

    print('Email is: '+ email)
    print('Password is:' + password)
    return 'DONE'

@app.route('/signup')
def show_signup():
    error =''
    if 'error' in session:
        error = session['error']
    return render_template('signup.html',error=error)

@app.route('/check_signup',methods=['POST'])
def check_signup():
    try:
        email = request.form['email']    
    except KeyError:
        email=''
    
    try:
        password = request.form['password']       
    except KeyError:
        password =''

    print('Email is: '+ email)
    print('Password is:' + password)

    
    if not len(email) > 0:
        session['error']='Email is required'
        return redirect('/signup')

    
    if not '@' in email or not '.' in email:
        session['error']='Email is invalid'
        return redirect('/signup')
    
    if not len(password)> 0:
        session['error']='password is required'
        return redirect('/signup')
    
    return redirect('/login')   
