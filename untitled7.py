s=["chandrapal","chand","characteristics","champ"]
n=len(s)
s.sort()
length=len(s[0])
result=""
final_result=''
for i in range(1):
    for j in range(length):
        if s[i][j]==s[i+1][j]:
            result=result+s[i][j]
for i in range(2,n):
    for j in range(len(result)):
        if result[j]==s[i][j]:
            
print(result)
'''['champ','chand','chandrapal','characteristics']'''
        