#!/usr/bin/env python
#coding:utf-8

def open_file(file_name):
    res={}
    with open(file_name) as f:
        for line in f:
            tmp=line.split(' ')
#           print tmp
            ip,url=tmp[0],tmp[6]
#       print ip,url 以元组的形式存到列表中
            res[(ip,url)]=res.get((ip,url),0)+1
    return sorted(res.items(),key=lambda  x:x[1],reverse=True)
#print open_file('log1.log')

def write_html(arr):
#拼接字符串
    count=0
    html_str='<table border="1px">'
    for i in arr[:10]:
        count=count+1
        html_str+='<tr><td>Num%s</td> <td>%s</td> <td>%s</td> <td>%s</td>' %(count,i[0][0],i[0][1],i[1])
    html_str+='</table>'
    html_f=open('res2.html','w')
    html_f.write(html_str)
    html_f.close()

def start_operate():
    res_list=open_file('log1.log')
    write_html(res_list)
start_operate()
