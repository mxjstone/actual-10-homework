#!/usr/bin/env python
#coding:utf-8
#冒泡排序
#  挨个对比，如果 一个元素比右边的大，交换位置
arr=[3,4,8,9,10,6,5,7]
length=len(arr)
for i in range(length):
	for j in range(length-1-i):
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
print arr
