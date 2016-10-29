#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
from hashlib import md5
from config import * 
import json
import db

salt = '890iop*()'
app.config.from_object(Table)
fields_duty = app.config.get('FIELDS_USER')

@app.route("/dutylist/")
def dutylist():
    if not session.get('name'):
	return render_template('/base/login.html')
    role = session.get('role')
    if role == 'admin':
	dutys = db.list('dutys',fields_duty)
	return render_template("/duty/dutylist.html",dutys = dutys,role = role)
    else:
        duty = db.list('dutys',fields_duty,session.get('id'))
        return render_template("/duty/dutyself.html",duty = duty,role = role)

@app.route("/dutyself/")
def dutyself():
    if not session.get('name'):
	return render_template('/base/login.html')
    role = session.get('role')
    id = session.get('id')
    duty = db.list('dutys',fields_duty,id)
    return render_template("/duty/dutyself.html",duty = duty,role = role)

@app.route("/dutyadd/",methods=['GET','POST'])
def dutyadd():
    if not session.get('name'):
	return redirect('/login')
    if request.method == 'GET':
	return render_template('/duty/add.html',role = session.get('role'))
    if request.method == 'POST':
	l = []
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	data['password'] = md5(request.form.get('password')+salt).hexdigest()

	for i in db.list('dutys',fields_duty):
	    l.append(i['name'])
	if not data['name']:
	    return json.dumps({'code':1,'errmsg':'name can not be null'})
	elif not data['name_cn']:
	    return json.dumps({'code':1,'errmsg':'chinese name can not be null'})
	elif not data['password']:
	    return json.dumps({'code':1,'errmsg':'password can not be null'})
	elif data['name'] not in l:
	    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	    db.add('dutys',conditions)
	    return json.dumps({'code':0,'result':'add duty success'})
	return json.dumps({'code':1,'errmsg':'dutyname is exist'})
