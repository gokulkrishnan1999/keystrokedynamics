from flask import Flask,render_template,request,session,redirect,url_for
from database import *
import demjson
import urllib
import numpy
import sklearn
from core import *
import uuid

app=Flask(__name__)
app.secret_key="val"

@app.route('/',methods=['get','post'])
def home():
	# val()

	return render_template('index.html')

@app.route('/home',methods=['get','post'])
def final():
	# val()

	return render_template('home.html')

@app.route('/register',methods=['get','post'])
def register():
	return render_template('register.html')

@app.route('/login',methods=['get','post'])
def login():
	return render_template('login.html')

@app.route('/user_home',methods=['get','post'])
def user_home():
	# gets=val(session['user_id'])
	gets=val(5)
	print(gets)
	if gets=="failed":
		return redirect(url_for('home'))
	return render_template('user_home.html')


@app.route('/login_action/',methods=['get','post'])
def login_action():
	data = {}
	if 'login' in request.form:
		name=request.form['username']
		features=request.form['features']
		print(features)
		s="select * from login inner join `user`using(login_id) where username='%s'"%(name)
		sel=select(s)
		if len(sel)>0:
			bool = get_login_id(features)
			print("dsf",bool)
			if bool != 1: 
				session['login_id'] = sel[0]['login_id']
				session['user_id'] = sel[0]['user_id']
				data['status'] = 'success'
				data['data'] = sel
			else:
				data['status'] = 'failed'
				data['reason'] = 'Time difference'
		else:
			data['status'] = 'failed'
			data['reason'] = 'Username  is incorrect'
	return demjson.encode(data)

@app.route('/register_action/',methods=['get','post'])
def register_action():
	if 'register' in request.form:
		print("haiii")
		fnam=request.form['fname']
		lnam=request.form['lname']
		ag=request.form['age']
		eml=request.form['email']
		phn=request.form['phone']
		user=request.form['user']
		features=request.form['features']
		lo="insert into login(username,features,usertype)values('%s','%s','user')"%(user,features)
		log=insert(lo)
		q="insert into `user`(login_id,fname,lname,age,email,phone)values('%s','%s','%s','%s','%s','%s')"%(log,fnam,lnam,ag,eml,phn)
		res=insert(q)
		train()
		

		return "ok"





app.run(debug=True,port=5002)







