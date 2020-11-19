def findWater(arr):
    low = 0
    high = len(arr) - 1
    left_max = 0
    right_max = 0
    water = 0
    while(low < high):
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                left_max = arr[low]
            else:
                water += left_max - arr[low]
            low += 1
        else:
            if arr[high] > right_max:
                right_max = arr[high]
            else:
                water += right_max - arr[high]
            high -=1

    return water

print(findWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2,1]))