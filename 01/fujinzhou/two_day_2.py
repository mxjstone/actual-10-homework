list1=[]
while True:
 x=raw_input('please input your name:')
 y=raw_input('please input your grade:')
 if y.isdigit() and x.isalpha():
    list1.append(str(x))
    list1.append(y)
 elif len(x)==0 or len(y)==0:
    print list1
    break
 else:
    print 'input is error'
