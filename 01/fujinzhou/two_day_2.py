#coding:utf-8
#用户输入名字和分数，并保存到list。如果输入为空，打印并结束循环。并算出平均值
list1=[]
count=0
num=0
while True:
 x=raw_input('please input your name:')
 y=raw_input('please input your grade:')
 if y.isdigit() and x.isalpha():
    list1.append(str(x))
    list1.append(int(y))
    count+=1
    num=(int(num)+int(y))/count
 elif len(x)==0 or len(y)==0:
    print list1
    break
 else:
    print 'input is error'
print '平均值是 %s' %(num)
