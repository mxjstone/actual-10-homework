# coding=utf-8
#!/usr/bin/env python

def grep_file():
    dict_up = {}
    with open('test.txt') as f:
        lines = f.readlines()
        for line in lines:
            dict_up[line.split(':')[0]] = line.split(':')[1]
    return dict_up


def regsiters(filename):
    while True:
        with open(filename, 'a+') as regsiter_file:
            username = raw_input('plases input username: ').strip()
            if username in grep_file().keys():
                print '用户名已存在'
                continue
            password = raw_input('plases input password: ').strip()
            print type(password)
            re_password = raw_input('plases input re password: ').strip()
            print type(re_password)
            if password == re_password:
                regsiter_file.write('%s:%s\n' % (username, password))
                return '注册成功'
                # break
            else:
                print '两次密码不相同'

print regsiters('test.txt')

	
