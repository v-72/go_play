"""
get me the contiguous largest subset of an array whose sum is 0
arr = [15, -2, 2, -8, 1, 7, 10, 23]
output: [-2, 2, -8, 1, 7]
"""

def zero_sub_seq(arr):
    sum = 0
    h = {}
    maxLen = 0
    subArr = []
    for i in range(len(arr)):
        sum = sum + arr[i]
        if(sum == 0):
            if maxLen < i:
                maxLen = i+1
        elif sum in h:
            if maxLen < i - h[sum]:
                maxLen = i-h[sum]
        else:
            h[sum] = i
            
    return maxLen


def zero_sub_seq_n2(arr):
    maxLen = 0
    subArr = []
    for i in range(len(arr)):
        sum = 0
        subarr = []
        for j in range(i,len(arr)):
            sum = sum + arr[j]
            if(sum == 0):
                if len(arr[i:j+1]) > len(subarr):
                    subarr = arr[i:j+1]
                maxLen = max(maxLen, j-i+1)
        if len(subArr) < len(subarr):
            subArr = subarr
    return subArr

arr = [15, -2, 2, -8, 1, 7, 10, 23]

print(zero_sub_seq_n2(arr))