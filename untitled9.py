arr=[6,-1,-3,4,-2,2,4,6,-12,-7]
n=len(arr)
count=0
result=0
for i in range(n):
    if arr[i]==0:
        result=result+1
for i in range(n-1):
    count=count+(arr[i]+arr[j])
        if count==0:
            result=result+1
print(result)        
    
        