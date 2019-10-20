# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:03:23 2019

@author: raj.kumar2208@yahoo.in

STack implementation using Array
"""

class StackArray:
    def __init__(self,limit=10):
        self.limit = limit
        self.arr = []
        
    def push(self,data):
        if len(self.arr) >= self.limit:
            raise ValueError("Stack Overflow")
        else:
            self.arr.append(data)
        print("Stack After Push: ", self.arr)
    
    def is_empty(self):
        if len(self.arr) == 0:
            return True
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        else:
            return self.arr.pop()
    
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        else:
            return self.arr[-1]
    
    def stack_size(self):
        return len(self.arr)
    
    def print_stack(self):
        print(self.arr)

if __name__ == "__main__":
    stack_one = StackArray(5)
    print(stack_one.is_empty())
    stack_one.push(5)
    stack_one.push(6)
    stack_one.push(7)
    print(stack_one.peek())
    stack_one.pop()
    stack_one.print_stack()
    
    
