# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:36:42 2019

@author: raj.kumar2208@yahoo.in

Infix to Postfix Expression Conversion using Stack

for this we have create a table in which operational precedence should be
defined
"""

class stack:
    def __init__(self):
        self.arr = []
    
    def push(self,data):
        self.arr.append(data)
    
    def pop(self):
        return self.arr.pop()
    
    def peek(self):
        return self.arr[-1]
    
    def __str__(self):
        return str(self.arr)
    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

def infix_to_postfix_conversion(string):
    """ First we set the precedence of operator and then implement 
    algorithm """
    pred = {}
    pred['*'] = 3
    pred['/'] = 3
    pred['+'] = 2
    pred['-'] = 2
    pred['('] = 1
    
    stack_output = stack()
    postfixList = []
    token = string.split()
    for i in token:
        if i in "QWERASDFZXCVTYUIOPGHJKLBNM0123456789":
            postfixList.append(i)
        elif i == '(':
            stack_output.push(i)
        elif i == ")":
            topi = stack_output.pop()
            while topi != "(":
                postfixList.append(topi)
                topi = stack_output.pop()
        else:
            while (not stack_output.is_empty() and
                   pred[stack_output.peek()] >= pred[i]):
                postfixList.append(stack_output.pop())
            stack_output.push(i)
    while not stack_output.is_empty():
        postfixList.append(stack_output.pop())
    return "".join(postfixList)

if __name__ == "__main__":
    print(infix_to_postfix_conversion("A + B + C * D"))
    print(infix_to_postfix_conversion("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infix_to_postfix_conversion("( A + B + C * ( D * E / F ) )"))