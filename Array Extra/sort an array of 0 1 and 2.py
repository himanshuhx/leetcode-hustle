# First Approach O(Nlogn) O(1) normal sorting

# Second Approach use counting sort
# in one traversal get count of 0, 1, 2
# in another traversal copy 0, 1, 2 respectively 

# Third Approach
# Dutch National Flag Algorithm
# O(N), O(1)

def sortList(arr):
    low, mid , high = 0, 0, len(arr)-1
    while mid<=high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input())) 
print(sortList(arr))