def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i]<arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
print(bubble([11,3,1,6,2,34,1,66]))