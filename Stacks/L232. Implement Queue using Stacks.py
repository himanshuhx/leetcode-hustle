# T.C push - O(1) pop- 0(1) amortized
# how?
# maintain two queue 
# first one for ---> pop()
# second one for ---> push()
# what is amortized analysis? if one operation is ON and rest time we do this operation
# it is O1 than we can say that we are having amortized O1 time complexity for this operation
# How pop() is o1?? initially both pop and push stacks are empty
# if push happens we simply push it to second stack
# first time when pop happens we empty our second array and append eerything to stack1
# thats why this empty operation is ON which happens not all time
# if we want to pop we pop from stack1 
# if we want to push push it to stack2

# another important point -- this two stack implementation for queue happens in real
# life when multi threading is involved for only read operation we dont want to give
# full lock of stack object therefore one is used for write and one for read 

class MyQueue:


    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)

    def pop(self) -> int:
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

    def peek(self) -> int:
         if self.stack1:
                return self.stack1[-1]
         else:
             return self.stack2[0]

    def empty(self) -> bool:
        return not self.stack2 and not self.stack1