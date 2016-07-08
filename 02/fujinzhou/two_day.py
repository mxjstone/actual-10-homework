#coding:utf-8
#用户输入名字和分数，并保存到list。如果输入为空，打印并结束循环。并算出平均值
list1=[]
count=0
num=0
while True:
 x=raw_input('please input your name:')
 y=raw_input('please input your grade:')
 if y.isdigit() and x.isalpha():
    list1.append(int(y))
    list1.append(str(x))
    count+=1
    num=int(num)+int(y)
 elif len(x)==0 or len(y)==0:
    avg=num/count
    print list1
    break
 else:
    print 'input is error'
print '平均值是 %s' %(avg)

#list最重要的一个特点：有序。 通过索引获取值   列表[索引]
#索引前面是从0开始，后面是从-1 开始

#list 是一个内置函数，不要以它命名
#arr = ['C','python','js','css','html','node']
#print arr[-6]
#arr1=list('python')
#print arr1
#for i in ['wd','pc','wn']:
#	print i
#print 'wd' in ['wd','pc'] 
#print 'wn' in ['wd','pc'] 
arr=[1,2,3,4,5,6]
#print len(arr)
#print max(arr)
#print min(arr)
#len(列表)返回列表的长度 min 最小值，max最大值
del arr[3]
print arr
#修改 根据索引找到值，并重新赋值
arr[0]='hello'
print arr

