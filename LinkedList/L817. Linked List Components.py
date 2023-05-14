class Solution:
    def numComponents(self, head, nums) -> int:
        setNums = set(nums)
        curr = head
        ans = 0
        while curr:
            if curr.val in setNums and (curr.next==None or curr.next.val not in setNums):
                ans += 1
            curr = curr.next
        return ans