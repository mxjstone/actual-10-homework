#!/usr/bin/env python
# coding=utf-8
ips = []
dict_ip = {}
num = 0
f = open('access.log')
nginx_files = open('nginx_file', 'a+')
nginx_lines = f.readlines()
for nginx_line in nginx_lines:
    ips.append(nginx_line.split()[0])
for ip in ips:
    if ip in dict_ip:
        dict_ip[ip] += 1
    else:
        dict_ip[ip] = 1
f.close()

dict_ips = dict((v, k) for k, v in dict_ip.iteritems())
keys = dict_ips.keys()
keys.sort()
keys.reverse()
for i in keys:
    num += 1
    if num == 1:
        nginx_files.write('''<!DOCTYPE html>
<head>
<meta charset="utf-8">
</head>
<html>
<body>
<table border='1'>
    <tr>
        <th>访问量</th>
        <th>IP</th>
    </tr>
    <tr>
        <td>%d</td>
        <td>%s</td>
    </tr>''' % (i, dict_ips[i])
                          )
        continue
    nginx_files.write('''
    <tr>
        <td>%d</td>
        <td>%s</td>
    </tr>''' % (i, dict_ips[i])
                          )
    if num == 10:
        nginx_files.write('''</table>
</body>
</html>
                        ''')
        break
nginx_files.close()



