# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:06:42 2019

@author: raj.kumar2208@yahoo.in

We perform all the required operation on double linked list 
1) Insertion
2) Deletion
3) Traversing
4) Print Reverse
5) Reverse
"""
class Node:
    def __init__(self, data=None, next_p=None, prev=None):
        self.data = data
        self.next_p = next_p
        self.prev = prev
    
    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    
    def set_next(self,next_p):
        self.next_p = next_p
    def get_next(self):
        return self.next_p
    
    def set_prev(self,prev):
        self.prev = prev
    def get_prev(self):
        return self.prev
    
    def has_next(self):
        return self.next_p != None
    def has_prev(self):
        return self.prev != None

def traversing_count(linkedlist):
    count = linkedlist.length
    current = linkedlist.head
    while current is not None:
        print("Data is: "+str(current.get_data()))
        current = current.get_next()
    print("count is: "+str(count))

class DoubleLL:
    
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
        self.length = 0
    
 
    
    def insert_at_start(self,data):
        new_node = Node(data)
        if ((self.length == 0) & (self.head == None)):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            new_node.set_prev(None)
            self.head = new_node
        self.length +=1
        
    def insert_at_end(self,data):
        new_node = Node(data)
        if ((self.length == 0) & (self.head == None)):
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while(current.get_next() != None):
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_next(None)
            new_node.set_prev(current)
            self.tail = new_node
        self.length +=1
        
    def insert_at_pos(self,data,pos):
        if ((pos <= 0) | (pos > self.length)):
            raise ValueError("Entered position value is incorrect")
        elif pos ==1:
            self.insert_at_start(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            previous = self.head
            current = self.head
            count = 1
            while (count < pos):
                count += 1
                previous = current
                current = current.get_next()
            previous.set_next(new_node)
            current.set_prev(new_node)
            new_node.set_next(current)
            new_node.set_prev(previous)
            self.length +=1
    
    def delete_at_start(self):
        if ((self.length == 0) & (self.head == None)):
            raise ValueError("List is Empty")
        else:
            previous = self.head
            current = self.head
            current = current.get_next()
            self.head = current
            previous.set_next(None)
            current.set_prev(None)
            self.length -= 1
    
    def delete_at_end(self):
        if((self.length == 0) & (self.head == None)):
            raise ValueError("List is Empty")
        else:
            previous = self.head
            current = self.head
            while(current.get_next() != None):
                previous = current
                current = current.get_next()
            previous.set_next(None)
            current.set_prev(None)
            self.length -= 1
    
    def delete_at_pos(self,pos):
        if ((self.length == 0) | (self.head == None)):
            raise ValueError("List is Empty")
        elif ((pos < 0) | (pos > self.length)):
            raise ValueError("Check the entered position: "+str(pos))
        elif pos == 1:
            self.delete_at_start()
        elif pos == self.length:
            self.delete_at_end()
        else:
            previous = self.head
            current = self.head
            count = 1
            while (count < pos):
                count += 1
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
            current.set_prev(None)
            temp = current
            current = current.get_next()
            current.set_prev(previous)
            temp.set_next(None)
            self.length -=1


    def print_reversing(self):
        current = self.tail
        count = self.length
        while (count !=0):
            print("Reverse Data is: "+str(current.get_data()))
            current = current.get_prev()
            count -=1

    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.get_prev()
            current.set_prev(current.get_next())
            current.set_next(temp)
            current = current.get_prev()
            if temp is not None:
                self.head = temp.get_prev()
            
    


    
if __name__=="__main__":
    mylist = DoubleLL()
    mylist.insert_at_start(5)
    mylist.insert_at_end(6)
    mylist.insert_at_end(7)
    mylist.insert_at_pos(1,1)
    mylist.insert_at_pos(8,4)
    mylist.insert_at_pos(10,2)
    traversing_count(mylist)
    mylist.reverse()
    traversing_count(mylist)
    