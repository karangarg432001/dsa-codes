def zigZag(arr, n):
	flag = 0
	for i in range(n-1):
		if flag==0:
			if arr[i] > arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
		else:	
			if arr[i] < arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
		flag = 1
	print(arr)
arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
zigZag(arr, n)