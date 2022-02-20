arr=[6,-1,-3,4,-2,2,4,6,-12,-7]
n=len(arr)
res=0
for i in range(n):
    sum_=0
    for j in range(i,n):
        sum_+=arr[j]
        if sum_==0:
            res+=1
print(res)    