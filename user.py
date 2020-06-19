from flask import *
from database import *
user=Blueprint("user",__name__)
@user.route('/user_home', methods=['get','post'])
def user_home():
	return render_template("user_home.html")


@user.route('/booking',methods=['get','post'])
def booking():
	data={}
	logid=session['logid']
	if 'submit' in request.form:
		sdate=request.form['starting_date']
		stime=request.form['starting_time']
		edate=request.form['ending_date']
		etime=request.form['ending_time']
		slot=request.form['slot']
		q="select amount from slots where slot_id='%s'"%(slot)
		s=select(q)
		amnt=s[0]['amount']
		# print(amnt)
		data['amnt']=amnt
		q="INSERT INTO booking VALUES(NULL,(select user_id from users where log_id='%s'),'%s','%s','%s','%s','%s','%s','NA')"%(logid,sdate,stime,edate,etime,slot,amnt)
		bookid=insert(q)
		return render_template("user_payment.html",data=data)
	q="select * from slots"
	res=select(q)
	data['slots']=res
	return render_template("user_booking.html",data=data)


@user.route('/payment',methods=['get','post'])
def payment():
	data={}
	logid=session['logid']
	q="select amount from booking where book_id=(select book_id from booking where user_id=(select user_id from users where log_id='%s')" %(logid)
	if 'submit' in request.form:
		amt=request.form['amount']
		mod=request.form['mode_of_payment']
		date=request.form['date']
		q="INSERT INTO payment VALUES(NULL,(select book_id from booking where user_id=(select user_id from users where log_id='%s')),'%s','%s','%s','NA')"%(logid,amt,mod,date)
		insert(q)
	return render_template("user_payment.html",data=data)


@user.route('/profile' ,methods=['get','post'])
def profile():
	data={}
	q="select * from users"
	res=select(q)
	data['profile']=res
	return render_template("user_profile.html",data=data)

