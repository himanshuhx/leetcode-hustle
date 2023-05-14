# normal edition
def binarySarch(arr, target):
    low, high = 0, len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# template edition
def binarySearch(arr,target):
    left, right = 0 , len(arr)-1
    while left<right:
        mid = left + (right-left)//2
        if arr[mid]==target:
            return True
        if arr[mid]>target:
            right = mid
        else:
            left = mid + 1
    return False


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
target = int(input())
arr.sort()
print(binarySearch(arr, target))

