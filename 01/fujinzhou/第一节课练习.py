#coding:utf-8
#呵呵
#print 'hello world'
#x='hello world'
#print x
#x=raw_input('hello world')
#print x
#int
#print 2+3
#print 1+2*3
#print 8/3
#print 8/3.0
#print 8%3
#str  单双引号无却别
print 'hello world'
print "hello world"
print "I'am pythoner"
print 'I\'am pythoner'
#三个单引号 起声明作用
print '''
this 

is 
a
 test
'''
#字符串拼接
print 'hello '+'reboot'
print 'hello '*2

#字符串格式化
#数字(0, 1, ...)即代表format()里面的元素, 所以可以使用"."调用元素的方法;
x='fujinzhou'
y=22
h='good'
print 'Hi %s I am %d years old ,You are very %s'%(x,y,h)
print 'Hi '+ x +',You are very '+ h +'' 
print ('Hi {0} I am {1} years old,You are very {2}!'.format(x,y,h))
