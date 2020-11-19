def countSmall(arr):
    res =[]
    for i in range(0,len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            print(arr[i],arr[j])
            if(arr[i] > arr[j]):
                count += 1
        res.append(count)
    
    return res

print(countSmall([5,2,55,6,1,44,2,56,78,1,99]))