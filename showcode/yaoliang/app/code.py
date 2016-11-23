#!/usr/bin/python
#coding:utf-8

from flask import render_template,request,redirect,session
from . import app
from config import *
from utils import login_request
from werkzeug import secure_filename
import paramiko
import json,os,sys,re
import db

reload(sys)
sys.setdefaultencoding('utf-8')

app.config.from_object(RemoteHost)
app.config.from_object(Table)
fields_code = app.config.get('FIELDS_CODE')
fpath = '/usr/local/src/'
hosts = []

for i in app.config:
    if re.findall('HOST.',i):
        hosts.append(app.config.get(i))
    # hosts格式为[['192.168.1.100', 22, 'root', '123456'],['192.168.1.101', 22, 'root', '123456'],['192.168.1.102', 22, 'root', '123456']]

def trans(where,filename):
    ssh = paramiko.SSHClient()
    comm = '/root/test.sh '+where

    for i in hosts:
        # 文件传输
	tus = (i[0],i[1])
	t = paramiko.Transport(tus)
	t.connect(username=i[2],password=i[3])
	sftp = paramiko.SFTPClient.from_transport(t)
	sftp.put(where,'/tmp'+filename)
	t.close()
	   
        # 执行远程命令
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(i[0],i[1],i[2],i[3],timeout=10)
        stdin,stdout,stderr = ssh.exec_command(comm)
        ssh.close()

@app.route('/code/',methods=['GET','POST'])
@login_request.login_request
def code():
    role = session.get('role')
    if request.method=='GET':
	return render_template('/code/code.html',role=role)
    else:
	file = request.files.get('package')
	filename = secure_filename(file.filename)
	if '.' in filename and filename.split('.',1)[1] == 'zip':
	    where = os.path.join(fpath,filename)
	    file.save(where)
	else:
	    return render_template('/code/code.html',result='上传类型必须是zip压缩包!',role = role)

	data = dict((k,v[0]) for k,v in dict(request.form).items()) # message, key, project
	key = data.pop('key')
	data['update_persion'] = session.get('name')
	data['package'] = filename
	conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
	if key == 'abc' and data['project']:
	    try:
		trans(where,filename)
    		db.add('code',conditions)
    		return render_template('/code/code.html',result='更新成功!',role = role)
	    except Exception, e:
		errmsg = '失败信息 error: '+str(e)
    		return render_template('/code/code.html',result=errmsg,role = role)
	elif not data['project']:
	    return render_template('/code/code.html',result='必须选择工程名!',role = role)
	else:
	    return render_template('/code/code.html',result='许可码无效!',role = role)

@app.route('/codelist/')
@login_request.login_request
def codelist():
    role = session.get('role')
    codes = db.list('code',fields_code)
    return render_template("/code/codelist.html",codes = codes,role = role)
