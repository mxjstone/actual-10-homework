#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
from config import * 
from utils import login_request
import json
import db
import time
#from utils import myMail

app.config.from_object(Table)
app.config.from_object(MyEmail)
fields_job = app.config.get('FIELDS_OPS_JOBS')  
fields_user = app.config.get('FIELDS_USER')  
localemail = app.config.get('LOCAL_EMAIL')
passwd = app.config.get('LOCAL_PASSWD')
ISOTIMEFORMAT='%Y-%m-%d %X'

''' 
{'0':'未处理','1':'处理中','2':'完成','3':'失败'}
'''

@app.route('/joblist/')
@login_request.login_request
def joblist():
    role = session.get('role')
    jobs = db.list('ops_jobs',fields_job)
    list_jobs = []
    for job in jobs:
        if job['status'] == 0 or job['status'] == 1:
	    list_jobs.append(job)
    return render_template("/job/joblist.html",jobs = list_jobs,role = role)

@app.route('/jobhistory/')
@login_request.login_request
def jobhistory():
    role = session.get('role')
    jobs = db.list('ops_jobs',fields_job)
    history_jobs = []
    for job in jobs:
        if job['status'] == 2 or job['status'] == 3:
    	    history_jobs.append(job)
    return render_template("/job/jobhistory.html",jobs = history_jobs,role = role)

@app.route("/jobadd/",methods=['GET','POST'])
@login_request.login_request
def jobadd():
    name = session.get('name')
    id = session.get('id')
    if request.method == 'GET':
	return render_template('/job/jobadd.html',info = session,role = session.get('role'))
    else:
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	data['apply_persion'] = name

	if not data['apply_desc']:
	    return json.dumps({'code':1,'errmsg':'job description can not be null'})
	conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	db.add('ops_jobs',conditions)

#	# 获取申请人email地址
#        user = db.list('users',fields_user,id)
#	# 从用户列表获取邮箱账号和密码(暂时没有)
#        email,passwd = user['email'],user['password']
#	# 发送邮件(需要发件人账号密码，密码，收件人，正文)
#        myMail.mymail(email,passwd,localemail,data)

	return json.dumps({'code':0,'result':'apply job success'})

# 获取工单状态
@app.route('/job_status/')
@login_request.login_request
def job_status():
    id = request.args.get('id')
    job = db.list('ops_jobs',fields_job,id)
#    return json.dumps({'code':0,'result1':apply_desc,'result2':status})
    result1 = job['status']
    result2 = job['apply_desc']
    result3 = job['deal_desc']
    return json.dumps({'code':0,'result1':result1,'result2':result2,'result3':result3})

# 修改工单状态
''' 
{'0':'未处理','1':'处理中','2':'完成','3':'失败'}
'''
@app.route('/update_status/',methods=['POST'])
@login_request.login_request
def update_status():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    res = {}
    if data['status'] == '1':
	data['deal_persion'] = session.get('name')
#	# 获取申请人email地址
#        user = db.list('users',fields_user,session.get('id'))
#        email = user['email']
#        res['operate'] = 'Consent to apply'
#        res['job'] = 'Consent to apply'
#	# 发送邮件
#	myMail.mymail(localemail,passwd,email,res)
    else:
	data['deal_time'] = time.strftime(ISOTIMEFORMAT,time.localtime())
#	myMail.mymail()

    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    db.update('ops_jobs',conditions,data['id'])
    return json.dumps({'code':0,'result':'execute completed!'})
