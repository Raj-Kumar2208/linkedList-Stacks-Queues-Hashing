# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:04:38 2019

@author: rajkumar2208@yahoo.in

Here  we are going to perform all operation related to Singly
Linked List.
1) Insertion
2) Deletion
3) Traversing and Count
4) Reverse the linked list.
5) Searching
"""
class Node:
    # Default constructor
    def __init__(self):
        self.data = None
        self.next_p = None
    # set next pointer
    def set_next(self,next_p):
         self.next_p = next_p
    # get next pointer
    def get_next(self):
        return self.next_p
    
    #set data
    def set_data(self,data):
         self.data = data
    #get data
    def get_data(self):
        return self.data
    #return true if node points to next pointer
    def has_next(self):
        return self.next_p != None


class LinkedList:
    def __init__(self,head=None):
        self.length=0
        self.head = head
    
    def insert_at_beginning(self,data):
        new_node = Node()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length +=1
    
    def insert_at_end(self,data):
        new_node = Node()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current= current.get_next()
            current.set_next(new_node)
        self.length +=1
    
    def insert_at_position(self,data,pos):
        if ((pos <= 0) | (pos > self.length)):
            raise ValueError("Check Position value")
        elif ((self.length == 0) | (pos==1)):
            self.insert_at_beginning(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            new_node = Node()
            new_node.set_data(data)
            count = 1
            current = self.head
            while count != pos-1:
                count +=1
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            self.length +=1
    
    def delete_at_start(self):
        if self.length == 0:
            raise ValueError("Linked is Empty")
        else:
            current = self.head
            self.head = self.head.get_next()
            current.set_next(None)
            self.length -= 1
            
    def delete_at_pos(self,pos):
        if self.length == 0:
            raise ValueError("List is Empty")
        elif ((pos <= 0) | (pos > self.length)):
            raise ValueError("Check the value of position")
        elif pos == 1:
            self.delete_at_start()
        elif pos == self.length:
            self.delete_at_end()
        else:
            count =1
            previous = self.head
            current = self.head
            while count < pos:
                count +=1
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
            self.length -=1
                
                
            
    def delete_at_end(self):
        if self.length == 0:
            raise ValueError("List is Empty")
        else:
            previous = self.head
            current = self.head.get_next()
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
            self.length -= 1


    def delete_node(self,data):
        if self.length == 0:
            raise ValueError("List is EMpty")
        else:
            previous = None
            current = self.head
            found = False
            while not found:
                if current.get_data() == data:
                    found = True
                elif current is None:
                    print("Node not found")
                    break
                else:
                    previous = current
                    current = current.get_next()
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
                self.length -=1

    
    def searching_node_get_position(self,data):
        if self.length == 0:
            raise ValueError("List is Empty")
        else:
            current = self.head
            found = False
            count = 1
            while not found:
                if current.get_data() == data:
                    print("given node data: ",current.get_data(),count)
                    found = True
                elif current is None:
                    raise ValueError("Node not found")
                else:
                    current = current.get_next()
                    count +=1


#count number of element and print their value
def traversing_count(linkedlist):
    count = linkedlist.length
    current = linkedlist.head
    while current is not None:
        print("Data is: "+str(current.get_data()))
        current = current.get_next()
    print("count is: "+str(count))

def reverse_linked_list(linkedlist):
    prev = None
    next_p = None
    current = linkedlist.head
    while (current is not None):
        next_p = current.get_next()
        current.set_next(prev)
        prev = current
        current = next_p
    linkedlist.head = prev

if __name__ =="__main__":
    raj = LinkedList()
    raj.insert_at_end(10)
    raj.insert_at_position(20,1)
    raj.insert_at_end(2)
    raj.insert_at_end(30)
    raj.insert_at_end(60)
    raj.insert_at_end(70)
    raj.insert_at_end(80)
    traversing_count(raj)
    reverse_linked_list(raj)
    traversing_count(raj)
    

                
                
            

    
        
