def LS(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [1,2,3,4,5,6,7]
target = 7

print(LS(arr,target))