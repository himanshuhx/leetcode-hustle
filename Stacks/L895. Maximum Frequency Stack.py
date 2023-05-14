class FreqStack:
    
    # https://www.youtube.com/watch?v=0fRmVjxopiE
    # O(1) O(N) 
    def __init__(self):
        self.freqStack = {}
        self.freqCount = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        if val in self.freqCount:
            self.freqCount[val]+=1
        else:
            self.freqCount[val] = 1
        count = self.freqCount[val]
        if count>self.maxFreq:
            self.maxFreq = count
        if count in self.freqStack:
            self.freqStack[count].append(val)
        else:
            self.freqStack[count] = [val]
        

    def pop(self) -> int:
        val = self.freqStack[self.maxFreq].pop()
        if not self.freqStack[self.maxFreq]:
            self.maxFreq-=1
        self.freqCount[val]-=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()