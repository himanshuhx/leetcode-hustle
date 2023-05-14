class Solution:

    # O(N) O(1)
    def minInsertions(self, s: str) -> int:
        openBracket = 0
        insertions = 0
        i=0
        while True:
            if i>=len(s):
                break
            if s[i]=='(':
                openBracket+=1
            else:
                if i+1<len(s) and s[i+1]==')':
                    i+=1
                    if openBracket>0:
                        openBracket -= 1
                    else:
                        insertions+=1
                else:
                    if openBracket>0:
                        insertions+=1
                        openBracket-=1
                    else:
                        insertions+=2
            i+=1           
        insertions += (2*openBracket)
        return insertions
                