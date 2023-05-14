# Approach 1 O(n^2), O(1) check if each element can ne a majority element or not
# Approach 2 O(n), O(n) use hashmap to store (num,frequency) if freq>n//2 that is ans

# Approach 3 moore's voting algo
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate