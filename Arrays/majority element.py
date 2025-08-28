arr = [2,2,1,1,1,2,2]


dic ={}

for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
    else:
        dic[arr[i]]=1

print(dic)
a=max(dic.values())
for k,v in dic.items():
    if v>len(arr)//2:
        print(k)