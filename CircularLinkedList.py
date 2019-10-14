# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 08:36:31 2019

@author: raj.kumar2208@yahoo.in

Operation we performed here is:
    1) Insertion
    2) Deletion
    3) COunting
    4) Traversing
"""
class Node:
    def __init__(self,data=None,next_p=None):
        self.data = data
        self.next_p = next_p
    
    def set_next(self,next_p):
        self.next_p = next_p
    def get_next(self):
        return self.next_p
    
    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    
    def has_next(self):
        return self.next_p != None

class CircularLL:
    def __init__(self,head=None):
        self.head = head
        self.length =0
    
    def insert_at_start(self,data):
        new_node = Node(data)
        if self.length ==0:
            self.head = new_node
            new_node.set_next(new_node)
        else:
            new_node.set_next(new_node)
            current = self.head.get_next()
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_next(self.head)
            self.head = new_node
        self.length +=1
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            new_node.set_next(new_node)
        else:
            new_node.set_next(new_node)
            current = self.head.get_next()
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_next(self.head)
        self.length +=1
    
    def delete_at_start(self):
        if self.length == 0:
            raise ValueError("List is Empty")
        else:
            temp = self.head
            current = self.head.get_next()
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(temp.get_next())
            self.head = temp.get_next()
            temp.set_next(None)
            self.length -= 1
            
            
    def delete_at_end(self):
        if self.length ==0:
            raise ValueError("List is EMpty")
        else:
            current = self.head.get_next()
            previous = self.head.get_next()
            while current.get_next() != self.head:
                previous = current
                current = current.get_next()
            previous.set_next(self.head)
            current.set_next(None)
            self.length -=1
            
  #here in reverse logic i am not changing head node
#sample input A--> B --> C --> D --> back to A
#sample output A --> D --> C --> B --> back to A          
    def reverse(self):
        current = self.head.get_next()
        prev = self.head
        next_p = None
        while current != self.head:
            next_p = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_p
        self.head.set_next(prev)
            
            
            
def traversing_count(clist):
    count = clist.length
    print("Count is: "+str(count))
    temp = clist.head
    while count != 0:
        print("Data is: "+str(temp.get_data()))
        temp= temp.get_next()
        count -= 1

if __name__ == "__main__":
    clist = CircularLL()
    clist.insert_at_end(2)
    clist.insert_at_start(3)
    clist.insert_at_start(4)
    clist.insert_at_start(5)
    clist.insert_at_start(6)
    clist.insert_at_start(7)
    traversing_count(clist)
    clist.reverse()
    traversing_count(clist)
    


    
        