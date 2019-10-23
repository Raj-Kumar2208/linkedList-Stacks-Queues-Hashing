# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:00:38 2019

@author: raj.kumar2208@yahoo.in

Stack Implementation based on LinkedList

Insertion and Deletion only happend at start

"""
class Node:
    def __init__(self,data,next_p=None):
        self.data = data
        self.next_p = next_p
    
    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    
    def set_next(self,next_p):
        self.next_p = next_p
    def get_next(self):
        return self.next_p
    
    def has_next(self):
        return self.next_p!= None

class StackLinkedList:
    def __init__(self,head=None):
        self.head = head
        self.length = 0
    
    def push(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            new_node.next_p = None
        else:
            new_node.next_p = self.head
            self.head = new_node
        self.length +=1
    
    def pop(self):
        if self.head == None:
            print("stack underflow")
        else:
            current = self.head
            self.head = current.get_next()
            current.set_next(None)
    
    def peek(self):
        if self.head == None:
            print("Stack Underflow")
        else:
            print("top data is: ", self.head.get_data())
            return self.head.get_data()
    
    def print_stack(self):
        current = self.head
        while current is not None:
            print("stack: ", current.get_data())
            current = current.get_next()

if __name__=="__main__":
    stack = StackLinkedList()
    stack.pop()
    stack.peek()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.peek()
    