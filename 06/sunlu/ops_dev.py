# coding=utf8
from flask import Flask, redirect, request, render_template, sessions, jsonify
import mysql_info as mysql
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    all_error = 'Account or password error'
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        if mysql.check_users(username, password) == 0:
            return redirect('/userlist?name=%s' % (username))
        return render_template('index.html', error=all_error)
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    error = 'Account already exists'
    error1 = 'passwd error'
    if request.method == 'POST':
        username = request.form['username']
        name_cn = request.form['name']
        password = request.form['password']
        re_password = request.form['re_password']
        email = request.form['email']
        tel = request.form['tel']
        role = request.form['selects']
        status = request.form['status']

        user_list = mysql.users_all()
        for user in user_list:
            if username in user['name']:
                return render_template('add.html', error=error)
        if password != re_password:
            return render_template('add.html', error=error1)
        mysql.insert_user(username, name_cn, password, email, tel, role, status, mysql.nowtime(), mysql.nowtime())
        return redirect('/userlist?name=%s' % (username))

    else:
        return render_template('add.html')


@app.route('/userlist', methods=['GET', 'POST'])
def userlist():
    del_id = request.args.get('delid')
    up_id = request.args.get('upid')
    users = mysql.users_all()
    if del_id:
        mysql.del_user(del_id)
        return redirect('/userlist')
    elif up_id:
        return redirect('/update?id=%d' %(int(up_id)))
    else:
        return render_template('userlist.html', users=users)


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        l = []
        d = {}
        ids = int(request.args.get('id'))
        d['name'] = request.form['name']
        d['password'] = request.form['password']
        d['email'] = request.form['email']
        d['mobile'] = request.form['tel']
        d['role'] = request.form['selects']
        d['status'] = request.form['status']
        for k, v in d.iteritems():
            l.append('%s="%s"' % (k, v))
        sql = 'update users set %s where id=%s' % (','.join(l), ids)
        db = MySQLdb.connect(host='192.168.1.7', user='root', passwd='123456', db='ops', charset='utf8')
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        cur.close()
        return redirect('/userlist?name=%s'%(d['name']))
    else:
        ids = int(request.args.get('id'))
        users = mysql.upuser_dict(ids)
        return render_template('update.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
