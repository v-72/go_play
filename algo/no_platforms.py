def count_no_platforms(arr,dep):
    no_platforms = 1
    result = 1
    n = len(arr)
    i = 1
    j = 0
    while(i<n and j<n):
        if (arr[i] <= dep[j]): 
            no_platforms+= 1
            i+= 1 
        elif (arr[i] > dep[j]): 
            no_platforms-= 1
            j+= 1
        if (no_platforms > result): 
            result = no_platforms 
        
    return result

arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 

print(count_no_platforms(arr,dep))