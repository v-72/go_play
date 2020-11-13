def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[min] > arr[j]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

print(selection([23,1,33,4,55,6,89]))