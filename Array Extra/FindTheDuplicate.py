# Approach 1 sort and check
# Approach 2 use set
# Approach 3 slow and fast 

def duplicate(arr):
    slow = fast = arr[0]
    firstIteration = True
    while slow!=fast or firstIteration:
        slow = arr[slow]
        fast = arr[arr[fast]]
        firstIteration = False

    fast = arr[0]
    while slow!=fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    return arr[slow]


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(duplicate(arr))