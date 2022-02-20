def maxWater(arr, n) :
    res = 0
    for i in range(1, n - 1) :
        left = arr[i]
        for j in range(i) :
            left = max(left, arr[j])
            right = arr[i]
        for j in range(i + 1 , n) :
            right = max(right, arr[j])
            res = res + (min(left, right) - arr[i])	
        return res
arr=[6,4,7,0,5,0]
n=len(arr)
print(maxWater(arr,n))
