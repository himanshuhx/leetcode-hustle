class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res, i, acc = 0, 0, 0
        for j in range(len(customers)):
            acc += customers[j] if grumpy[j] == 1 else 0
            if j-i+1 == X:
                res = max(res, acc)
                acc -= customers[i] if grumpy[i] == 1 else 0
                i += 1
        return res + sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)