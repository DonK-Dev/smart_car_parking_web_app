from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
	return render_template("home.html")
@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']

		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['logid']=res[0]['log_id']
			if res[0]['type']=='admin':
				return redirect(url_for('admin.home'))
			if res[0]['type']=='user':
				return redirect(url_for('user.user_home'))

	return render_template("login.html")


@public.route('/reg',methods=['get','post'])
def reg():
	if 'submit' in request.form:
		fname=request.form['first_name']
		lname=request.form['last_name']
		hname=request.form['house_name']
		place=request.form['place']
		pincode=request.form['pincode']
		lat=request.form['latitude']
		lon=request.form['longitude']
		phn=request.form['phone']
		email=request.form['email']
		uname=request.form['username']
		pwd=request.form['passwword']
		q="SELECT * FROM login WHERE username='%s' AND password='%s'" %(uname,pwd)
		res=select(q)
		if res:
			flash("Details already exists.")
		else:
			q="insert into login values(null,'%s','%s','user')"%(uname,pwd)
			id=insert(q)
			q="INSERT INTO users VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,hname,place,pincode,lat,lon,phn,email)
			insert(q)
			flash("Registration successful")
	return render_template("registration.html")


@public.route('/loc',methods=['get','post'])
def loc():
	data={}
	q="select * from parking_locations"
	res=select(q)
	data['view'] =res
	return render_template("parking.html",data=data)