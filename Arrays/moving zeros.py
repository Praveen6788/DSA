arr =[1,0,2,0,12,0,0,0]
j=len(arr)

i=0
for j in range(len(arr)):
    if arr[j]!=0:
        arr[i]=arr[j]
        i+=1
    
    
while (i<len(arr)):
    arr[i]=0
    i+=1
        


print(arr)