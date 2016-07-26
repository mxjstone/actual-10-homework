#!/usr/bin/env python
#coding:utf-8
#函数的概念： 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段

#定义函数的规则：函数代码块以def 关键字开头，后面接函数标识符名称和圆括号（）
#任何传入参数和自变量 必须放在圆括号中间，圆括号中间可以用于定义参数
#函数的内容以冒号起始，并且缩进。
#return（表达式）结束函数，选择性的返回一个值给调用方。

#小栗子
def hello(name):
    print "hello %s" %(name)
hello(name="fujinzhou")
hello(name="reboot")

#不定长参数
#惨了星号的变量名会存放所有未命名的变量参数
def prininfo(arg1,*vartuple):
    print "输出 ："
    print arg1
    print vartuple
    return
prininfo(10,20,30,40)

#匿名函数lambda 是一个表达式
#lambda [arg1 [,arg2,.....argn]]:语句

#函数说明
sum1=lambda arg1,arg2:arg1*arg2
#调用sum1函数
print "相乘后的值为:",sum1(10,29)

#return 语句
#return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。

#函数说明
def count(arg1,arg2):
    total=arg1+arg2
    print "函数内：",total
    return total
#调用count函数
total=count(10,20)
print "函数外:",total

#变量作用域 一个程序的所有变量并不是在哪个位置都可以访问的。访问权限取决于这个变量在哪里赋值

#全局变量和局部变量
#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
#局部变量只能在被声明的函数内部访问，全局变量在整个程序都可以访问

#这是一个全局变量
total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print "函数内部是局部变量：",total
    return total

sum(10,20)
print "函数外部是全局变量:",total
