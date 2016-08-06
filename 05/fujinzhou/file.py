#!/usr/bin/env python
#coding:utf-8
def userinfo():
    res={}
    with open('user.txt') as f:
        for line in f:
            tmp=line.strip().split(":")
            res[tmp[0]]=tmp[1]
    return res
#print userinfo()

def adduser(user,password):
	with open('user.txt','a+') as f:
		f.write("%s:%s\n"%(user,password))

def checkinfo (user,password):
	if len(user) !=0  and len(password)!=0:
		return True
