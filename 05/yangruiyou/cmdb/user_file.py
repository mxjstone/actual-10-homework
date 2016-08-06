#coding:utf-8
import pickle


def Create():
    users = {'panda': '123456', 'woniu': '123456', 'kk': 'kk'}
    fo = open('users.txt', 'wb')
    pickle.dump(users, fo)
    fo.close()


def Delete():
    content = {}
    f = open('users.txt')
    content = pickle.load(f)
    f.close()
    content.pop('kk')
    f = open('users.txt', 'wb')
    pickle.dump(content, f)
    f.close()


def Modify():
    content = {}
    f = open('users.txt')
    content = pickle.load(f)
    f.close()
    content['pc'] = '666666'
    f = open('users.txt', 'wb')
    pickle.dump(content, f)
    f.close()


def Select():
    content = {}
    f = open('users.txt')
    content = pickle.load(f)
    f.close()
    print content
    for k, v in content.items():
        print "用户信息:%s--->%s" % (k, v)

def SelectOne(username):
    name = username
    content = {}
    userinfo = {}
    f=open('users.txt')
    content =pickle.load(f)
    f.close()
    userinfo[name]=content[name]
    print userinfo
    return userinfo


Create()
Delete()
Modify()
Select()
SelectOne('panda')


