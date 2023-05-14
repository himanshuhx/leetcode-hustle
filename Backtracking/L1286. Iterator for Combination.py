# https://www.youtube.com/watch?v=UOy4IAjvajY

from collections import deque
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.queue = deque()
        self.generate(characters, combinationLength, 0, [])
        print(self.queue)
        
    def generate(self, s, k, i, curr):
        if k==0:
            self.queue.append(''.join(curr))
            return
        
        for j in range(i,len(s)):
            curr.append(s[j])
            self.generate(s, k-1, j+1, curr)
            curr.pop()

    def next(self) -> str:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue)>0

