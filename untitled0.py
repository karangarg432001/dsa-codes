def chocolate(arr,n,m):
    arr.sort()
    result=99999
    for i in range((n-m)+1):
        if i<n-m:
            max_=arr[m+i-1]
            min_=arr[i]
            if result>(max_-min_):
                result=max_-min_  
    return result
arr=[3,4,1,9,56,7,9,12]
n=len(arr)
m=5
print(chocolate(arr, n, m))
"[1, 3, 4, 7, 9, 9, 12, 56]"