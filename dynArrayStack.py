# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 20:40:00 2019

@author: raj.kumar2208@yahoo.in

STack implementation based on Dynamic Array

Here we are going to array doubling technique
When array get full we increase its size by doubling it
"""

class StackDynaArray:
    def __init__(self,limit=2):
        """ please change the limit value for first array
        initilization"""
        self.limit = limit
        self.arr =[]
    
    def is_empty(self):
        if len(self.arr) == 0:
            return True
    
    def push(self,data):
        if len(self.arr) >= self.limit:
            self.resize()
        self.arr.append(data)
        print("Stack after push: ",self.arr)
    
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            return self.arr.pop()
    
    def peek(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            return self.arr[-1]
    
    def print_stack(self):
        print("stack is: ",self.arr)
        
    def resize(self):
        temp = self.arr
        self.limit = 2*self.limit
        self.arr = temp
    
    def stack_size(self):
        print("length of stack is: ", len(self.arr))

if __name__ == "__main__":
    stack = StackDynaArray()
    stack.pop()
    stack.print_stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.stack_size()
    stack.pop()
    stack.stack_size()
    print(stack.peek())
    stack.print_stack()
