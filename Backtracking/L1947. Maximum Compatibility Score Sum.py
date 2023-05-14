class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def getCompScore(sIdx, mIdx):
            compScore = 0
            for i in range(n):
                if students[sIdx][i]==mentors[mIdx][i]:
                    compScore+=1
            return compScore
        
        def solve(start, score):
            nonlocal maxScore
            if start>=len(students):
                maxScore = max(maxScore, score)
                return
            
            for j in range(len(mentors)):
                if mentorAvailable[j]:
                    mentorAvailable[j]=False
                    compScore = getCompScore(start, j)
                    solve(start+1, score+compScore)
                    mentorAvailable[j]=True
        
        maxScore = 0
        mentorAvailable = [True]*len(mentors)
        n = len(students[0])
        solve(0, 0)
        return maxScore
        