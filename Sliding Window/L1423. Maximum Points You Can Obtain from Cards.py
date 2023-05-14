class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[:k])
        maxi = total
        for i in range(k):
            total = total - cardPoints[k-1-i] + cardPoints[len(cardPoints)-1-i]
            maxi = max(maxi,total)
        return maxi