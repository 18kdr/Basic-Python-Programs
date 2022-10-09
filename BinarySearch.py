from cgitb import reset


def BinarySearch(arr,target,start,end):
    while end >= start:
        mid = (start + end)//2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] >= target:
            end = mid - 1
        elif arr[mid] <= target:
            start = mid + 1
        else:
            return -1

arr = [1,2,3,4,5,6,7,8]

target = 8

end = len(arr) - 1
result = BinarySearch(arr,target,0,end)

if result == target:
    print("Found")
else:
    print("Not Found")