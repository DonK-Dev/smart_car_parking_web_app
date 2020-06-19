from flask import *
from database import *
import qrcode
import uuid

admin=Blueprint('admin',__name__)
@admin.route('/home',methods=['get','post'])
def home():
	return render_template("admin_home.html")


@admin.route('/loc_reg',methods=['get','post'])
def loc_reg():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from parking_locations where loc_id='%s'"%(id)
		delete(q)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from parking_locations where loc_id='%s'"%(id)
		delete(q)
	if action=='update':
		q="SELECT * FROM parking_locations WHERE loc_id='%s'" %(id)
		data['up_loc']=select(q)
	if 'update' in request.form:
		lname=request.form['loc_names']
		place=request.form['places']
		lat=request.form['latitudes']
		lon=request.form['longitudes']
		des=request.form['descriptions']
		q="UPDATE parking_locations SET loc_name='%s',place='%s' ,latitude='%s',longitude='%s',description='%s' WHERE loc_id='%s'" %(lname,place,lat,lon,des,id)
		update(q)
		return redirect(url_for('admin.loc_reg'))
	if 'submit' in request.form:
		lname=request.form['loc_name']
		place=request.form['place']
		lat=request.form['latitude']
		lon=request.form['longitude']
		des=request.form['description']
	
		q="INSERT INTO parking_locations VALUES(NULL,'%s','%s','%s','%s','%s')"%(lname,place,lat,lon,des)
		insert(q)
	
	q="select * from parking_locations"
	res=select(q)
	data['view'] =res
	return render_template("admin_locregistration.html",data=data)

@admin.route('/slot_reg',methods=['get','post'])
def slot_reg():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from slots where slot_id='%s'"%(id)
		delete(q)
	if action=='update':
		q="SELECT * FROM slots inner join parking_locations using(loc_id) WHERE slot_id='%s'" %(id)
		data['slot_up']=select(q)
	if 'update' in request.form:
		locname=request.form['locnames']
		sdes=request.form['slot_descriptions']
		amt=request.form['amounts']
		q="UPDATE slots SET slot_description='%s',loc_id='%s',amount='%s' WHERE slot_id='%s'"%(sdes,locname,amt,id)
		update(q)
		return redirect(url_for('admin.slot_reg'))

	if 'submit' in request.form:
		locname=request.form['locname']
		sdes=request.form['slot_description']
		amt=request.form['amount']
		q="INSERT INTO slots VALUES(NULL,'%s','free','%s','%s','filename')"%(sdes,locname,amt)
		id=insert(q)
		path = "static/qrcode/" + str(uuid.uuid4()) + ".png"
		img = qrcode.make(id)
		img.save(path)
		q="UPDATE slots SET qr_code='%s' WHERE slot_id='%s'" %(path,id)
		update(q)
		return redirect(url_for('admin.slot_reg'))
	q="select * from parking_locations"	
	res=select(q)
	data['loc']=res
	q="select * from slots inner join parking_locations using(loc_id)"
	res=select(q)
	data['sv'] =res
	return render_template("admin_slotregistration.html",data=data)


@admin.route('/slot_status' ,methods=['get','post'])
def slot_status():
	data={}
	q="select * from slots inner join parking_locations using(loc_id) "
	res=select(q)
	data['sts']=res
	return render_template("admin_slotstatusview.html",data=data)

@admin.route('/reg_users' ,methods=['get','post'])
def reg_users():
	data={}
	q="select * from users"
	res=select(q)
	data['regu']=res
	return render_template("admin_viewregusers.html",data=data)


@admin.route('/book_info' ,methods=['get','post'])
def book_info():
	data={}
	q="select * from booking inner join slots using(slot_id) "
	res=select(q)
	data['bv']=res
	return render_template("admin_viewbookinginfo.html",data=data)

@admin.route('/view_payment' ,methods=['get','post'])
def view_payment():
	data={}
	q="SELECT CONCAT(first_name,' ',last_name) AS user_name,`booking`.`amount`,mode_of_payment,`date` FROM payment INNER JOIN booking USING(book_id) INNER JOIN users USING (user_id)"
	res=select(q)
	data['pay']=res
	return render_template("admin_payrep.html",data=data)

@admin.route('view_complaint' ,methods=['get','post'])
def view_complaint():
	data={}
	q="select concat(first_name,' ',last_name) as user_name,`description`,`date`,solution,complaint_id from complaint inner join users USING (user_id)"
	res=select(q)
	data['com']=res
	return render_template("admin_viewcomplaint.html",data=data)

@admin.route('/view_replay' ,methods=['get','post'])
def view_replay():
	data={}
	id=request.args['id']
	q="select *,concat(first_name,' ',last_name) as user_name from complaint inner join users using (user_id) WHERE complaint_id='%s'" %(id)
	res=select(q)
	print(res)
	data['vr']=res
	if 'submit' in request.form:
		solution=request.form['soln']
		q="UPDATE complaint SET solution='%s',status='replied' WHERE  complaint_id='%s'" %(solution,id)
		update(q)
		return redirect(url_for("admin.view_complaint")) 
	return render_template("admin_replay.html",data=data)