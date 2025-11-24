arr = [10, 22, 12, 3, 0, 6]
res =[]
for i in range(len(arr)):
    leader =  arr[i]
    for j in range(i+1,len(arr)):
        if arr[j]> arr[i]:
            leader= arr[j]
            break
    res.append(leader)

print(res)

