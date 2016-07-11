#coding=UTF-8
#插入排序
array = [3,1,4,2,5,7,6]
length = len(array)
for i in range(1,length):
    key = array[i]
    j = i-1 
    while array[j] > key and j >= 0:
        array[j+1] = array[j]
        j = j-1 
    array[j+1] =key
print array
