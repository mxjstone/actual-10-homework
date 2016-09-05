#coding:utf-8

import  MySQLdb as mysql

conn = mysql.connect(user='root',passwd='123456',host='localhost',db='reboot10')
cur = conn.cursor()

def list(table,fields,id=None):
    users = []
    if not id:
        sql = "select %s from %s"%(','.join(fields),table)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            user = {}
            for i,k in enumerate(fields):
                user[k] = row[i]
            users.append(user)
        return users
    else:
        sql2 = "select %s from %s where id='%s'"%(','.join(fields),table,id)
        cur.execute(sql2)
        result = cur.fetchone()
        user = {}
        for i,k in enumerate(fields):
            user[k] = result[i]
        return user

def add(table,args):
    sql = 'insert into %s set %s'%(table,','.join(args))
    cur.execute(sql)
    conn.commit()
    
def delete(table,id):
    sql = "delete from %s where id='%s'"%(table,id)
    cur.execute(sql)
    conn.commit()

def update(table,args,id):
    sql = "update %s set %s where id=%s"%(table,','.join(args),id)
    cur.execute(sql)
    conn.commit()
