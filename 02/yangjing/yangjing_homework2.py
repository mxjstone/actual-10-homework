arr = [13,15,37,89,60,39,12,109,56,72]
arr_length = len(arr)
n = 0
j = 0
for i in range(arr_length):
	print 'Compare round %s' % i
	print arr[j:arr_length]

	for j in range(i+1, arr_length):
		print 'compare %s with %s' %(arr[i], arr[j])
		if arr[i] < arr[j]:
			print 'no swap'
			print arr
		else:
			print 'swap %s  with %s' % (arr[i], arr[j])
			arr[i], arr[j] = arr[j], arr[i]
			print arr
			print ' new arr min number is %s' % arr[i]
		n += 1
	print '-----------------------------'
	print 'min number is %s' % arr[0]
	print '-----------------------------'
	n +=1

print arr
print n