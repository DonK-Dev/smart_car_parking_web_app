from flask import *
from database import *
import demjson 
from datetime import datetime
from datetime import *
import datetime

api=Blueprint('api',__name__)

@api.route('/login/')
def login():
	data={}
	username = request.args['username']
	password = request.args['password']
	print(username,password)
	q = "select * from login where username='%s' and password='%s'" % (username,password)
	res = select(q)
	# print(res)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	# print(data['status'])
	return demjson.encode(data)

@api.route('/register',methods=['get','post'])
def register():
	data={}
	fname = request.args['first_name']
	lname = request.args['last_name']
	house = request.args['house_name']
	place= request.args['place']
	pin = request.args['pincode']
	mail = request.args['email']
	phn = request.args['phone']
	uname = request.args['username']
	pwd = request.args['password']
	lati=request.args['lati']
	longi=request.args['longi']
	q="SELECT * FRom login where username='%s' and password='%s'"%(uname,pwd)
	res=select(q)
	if res:
		data['status']='duplicate'
	else:
		q = "INSERT into login values(NULL,'%s','%s','user')" % (uname,pwd)
		id = insert(q)
		q = "INSERT into users values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (id,fname,lname,house,place,pin,lati,longi,phn,mail)
		insert(q)
		data['status'] = 'success'
	return demjson.encode(data)

@api.route('/viewprofile/',methods=['get','post'])
def viewprofile():
	data={}
	log=request.args['login_id']
	q="SELECT * from users where log_id='%s' "%(log)
	res=select(q)
	if res:
		data['status']='success'
		data['data']=res
		data['method']='viewprofile'
	else:
		data['status']='failed'
		data['method']='viewprofile'
	return demjson.encode(data)

@api.route('/upprof',methods=['get','post'])
def upprof():
	data={}
	house = request.args['house_name']
	place= request.args['place']
	pin = request.args['pincode']
	mail = request.args['email']
	phn = request.args['phone']
	# print(phn)
	logid=request.args['logid']
	q="update users set house_name='%s',place='%s',pincode='%s',phone='%s',email='%s' where log_id='%s' "%(house,place,pin,phn,mail,logid)
	update(q)
	data['status']='success'
	data['method']='upprof'
	return demjson.encode(data)


@api.route('/viewparkloc')
def viewparkloc():
	data={}
	lati=request.args['lati']
	logi=request.args['logi']
	q="SELECT *,latitude,longitude,SQRT(POW(69.1 *(latitude-'%s'),2)+POW(69.1 *('%s'-longitude)*COS(latitude/57.3),2)) AS distance FROM `parking_locations` INNER JOIN `slots` USING(`loc_id`) HAVING distance<25 ORDER BY distance"  %(lati,logi)
	res=select(q)
	# print(res)
	if res:
		data['data']=res
		data['status']="success"
	else:
		data['status']='failed'
	return demjson.encode(data)

@api.route('/slot_booking')
def slot_booking():
	data={}
	data['method']='slot_booking'
	slot=request.args['slotid']
	log=request.args['logid']
	sd=request.args['sd']
	st=request.args['st']
	ed=request.args['ed']
	et=request.args['et']
	# print(sd,ed)
	# nows=datetime.now
	today = date.today()
	

	x=sd.split("-")
	y=ed.split("-")
	u=st.split(":")
	v=et.split(":")
	print(u,v)
	a=datetime.datetime(int(x[2]),int(x[1]),int(x[0]),int(u[0]),int(u[1]))
	b=datetime.datetime(int(y[2]),int(y[1]),int(y[0]),int(v[0]),int(v[1]))
	g=datetime.date(int(x[2]),int(x[1]),int(x[0]))
	h=datetime.date(int(y[2]),int(y[1]),int(y[0]))
	print(a,b)
	c=b-a
	days=c.days
	hours=c.seconds//3600
	minutes=(c.seconds//60)%60
	print(days)
	print(hours)
	print(minutes)
	if g<today:
		data['status']='failedsd'
	elif h<g:
		data['status']='faileded'
	else:
		q="SELECT amount FROM slots WHERE slot_id='%s'" %(slot)
		res=select(q)
		if(hours>1):
			amount=int(res[0]['amount'])*(days+1)
		else:
			amount=int(res[0]['amount'])*days
		q="INSERT INTO booking VALUES(NULL,(SELECT user_id FROM users WHERE log_id='%s'),'%s','%s','%s','%s','%s','%s','Reserved')" %(log,sd,st,ed,et,slot,amount)
		id=insert(q)
		q="INSERT INTO payment VALUES(NULL,'%s','%s','online',CURDATE(),'NA')" %(id,amount)
		insert(q)
		q="UPDATE slots SET slot_status='Reserved' WHERE slot_id='%s'" %(slot)
		update(q)
		data['status']='success'
	print(data['status'])
	return demjson.encode(data)

@api.route('/view_slots_pay')
def view_slots_pay():
	data={}
	data['method']='view_slots_pay'
	log=request.args['logid']
	q="SELECT *,`payment`.`status` as st FROM `booking` INNER JOIN `slots` USING(`slot_id`) INNER JOIN `parking_locations` USING(`loc_id`)inner join payment using(book_id) WHERE user_id=(SELECT user_id FROM users WHERE log_id='%s')" %(log)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	else:
		data['status']='failed'
	return demjson.encode(data)

@api.route('/view_amount')
def view_amount():
	data={}
	logid=request.args['logid']
	slotid=request.args['slotid']
	q="SELECT amount FROM `booking`  WHERE slot_id='%s'" %(slotid)
	res=select(q)
	if res:
		data['data']=res
		data['method']='view_amount'
		data['status']='success'
	else:
		data['status']='failed'
		data['method']='view_amount'
	return demjson.encode(data)

@api.route('/confirm_payment')
def confirm_payment():
	data={}
	data['method']='confirm_payment'
	logid=request.args['logid']
	slotid=request.args['slotid']
	bookid=request.args['bookid']
	q="UPDATE payment SET status='Done'  WHERE book_id='%s'" %(bookid)
	update(q)
	q="UPDATE booking SET status='Payed' WHERE book_id='%s'" %(bookid)
	update(q)
	data['status']='success'
	return demjson.encode(data)

@api.route('/view_complaints')
def view_complaints():
	data={}
	log=request.args['logid']
	q="SELECT * FROM complaint WHERE user_id=(SELECT user_id FROM users WHERE log_id='%s')" %(log)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
		data['method']='view_complaints'
	else:
		data['status']='failed'
		data['method']='view_complaints'
	return demjson.encode(data)

@api.route('/add_complaints')
def add_complaints():
	data={}
	log=request.args['logid']
	com=request.args['com']
	q="INSERT INTO complaint VALUES(NULL,(SELECT user_id FROM users WHERE log_id='%s'),'%s',CURDATE(),'Pending','NA')" %(log,com)
	insert(q)
	data['status']='success'
	data['method']='add_complaints'
	return demjson.encode(data)

@api.route('/view_qr_code/')
def view_qr_code():
	data={}
	qrid=request.args['qrid']
	logid=request.args['logid']
	q="SELECT * FROM `booking` INNER JOIN `slots` USING(`slot_id`) INNER JOIN `parking_locations` USING(`loc_id`) WHERE user_id=(SELECT user_id FROM users WHERE log_id='%s' )and slot_id='%s'" %(logid,qrid)
	res=select(q)
	if res:
		if res[0]['status']=='Payed':
			if res[0]['slot_status']=='Reserved':
				q="UPDATE slots SET slot_status='Occupied' Where slot_id='%s'" %(qrid)
				update(q)
				data['status']='Occupied'
				data['method']='view_qr_code'
			elif res[0]['slot_status']=='Occupied':
				q="UPDATE slots SET slot_status='free' WHERE slot_id='%s'" %(qrid)
				update(q)
				data['status']='free'
				data['method']='view_qr_code'
		else :
			data['status']='pending_payment'
	else:
		data['status']='failed'
	data['method']='view_qr_code'
	return demjson.encode(data)

@api.route('/viewnearestslots')
def viewnearestslots():
	data={}
	lati=request.args['lati']
	logi=request.args['logi']
	logid=request.args['logid']
	q="SELECT *,`parking_locations`.`latitude`,`parking_locations`.`longitude`,SQRT(POW(69.1 *(`parking_locations`.`latitude`-'%s'),2)+POW(69.1 *('%s'-`parking_locations`.`longitude`)*COS(`parking_locations`.`latitude`/57.3),2)) AS distance FROM `booking` INNER JOIN `users` USING(`user_id`) INNER JOIN `slots` USING(`slot_id`) INNER JOIN `parking_locations` USING(`loc_id`) WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `log_id`='%s')" %(lati,logi,logid)
	res=select(q)
	if res:
		data['data']=res
		data['method']='viewnearestslots'
		data['status']='success'
	else:
		data['method']='viewnearestslots'
		data['status']='failed'
	return demjson.encode(data)