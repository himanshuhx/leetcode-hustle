'''
return True if perfect square else return False

we will do binary search as the function is monotonic in nature

Time Complexity - O(logN)
Space Complexity - O(1)

'''

def binarySearch(num):
    low, high = 0 , num # making high to num
    while low<=high:
        mid = (low + high)//2
        square = mid * mid # checking square of mid and then taking steps acc to condition
        if num[mid] == square:
            return True
        elif square > num: # if square of mid is greater than num we know our ans is on left side
            high = mid-1
        else:              # ans is on right side
            low = mid+1
    return False