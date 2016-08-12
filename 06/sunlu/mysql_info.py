# coding=utf8
import MySQLdb
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

dbhost = '192.168.1.7'
dbuser = 'root'
dbpasswd = '123456'
database = 'ops'


def nowtime():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now

def check_users(username, password):
    users_list = users_all()
    for user in users_list:
        if username == user['name'] and password == user['password']:
            return 0
        else:
            pass



def gettables(tablename):
    tablenames = []
    db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=database, charset='utf8')
    cur = db.cursor()
    cur.execute('desc %s' % (tablename))
    for row in cur.fetchall():
        tablenames.append(row[0])
    cur.close()
    return tablenames


def users_all():
    users = []
    fields = gettables('users')
    sql = 'select %s from users' % (",".join(fields))
    db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=database, charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    for row in cur.fetchall():
        user = {}
        for k, v in enumerate(fields):
            user[v] = row[k]
        users.append(user)
    cur.close()
    return users


def insert_user(username, name_cn, password, email, tel, role, status, create_time, last_time):
    fields = ['name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status', 'create_time', 'last_time']
    d = dict(zip(fields, [username, name_cn, password, email, tel, role, status, create_time, last_time]))
    sql = 'insert into users (%s) values (%s)' % (
        ','.join(fields), ','.join(['"%s"' % d[i] for i in fields]))
    db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=database, charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    cur.close()



def del_user(ids):
    sql = 'delete from users where id=%d' % (int(ids))
    db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=database, charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    cur.close()


def upuser_dict(ids):
    d = {}
    fields = ['name', 'name_cn', 'password', 'email', 'mobile', 'role', 'status']
    users = users_all()
    for user in users:
        if ids == user['id']:
            for i in fields:
                d[i] = user[i]
    return d

