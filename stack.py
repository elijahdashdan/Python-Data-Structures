from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    


    
def reverseString(string):
    s = Stack()
    for char in string:
        s.push(char)

    reverseSTR = ""
    while s.size() !=0:
        reverseSTR += s.pop()
        
    return reverseSTR


# print(reverseString("We will conquer COVID-19"))

