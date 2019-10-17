# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:53:53 2019

@author: raj.kumar2208@yahoo.in
"""


import random
import math

class Node:
    def __init__(self,data,level=0):
        self.data = data
        self.next_p = [None]*level
        
    
class SkipList:
    def __init__(self,max_level=8):
        self.max_level = max_level
        n = Node(None,max_level)
        self.head = n
        self.no_of_element = 1
        self.verbose = False
    
    def random_level(self,max_level):
        num = random.randint(1,2**max_level-1)
        lognum = math.log(num,2)
        level = int(math.floor(lognum))
        return max_level - level
    
    def update_vector(self,data):
        update = [None]*self.max_level
        n = self.head
        self.n_traverse = 0
        level = self.max_level -1
        
        while level >= 0:
            if self.verbose and n.get_next()[level] != None and n.next_p[level].data >= data:
                print("Drop down from level ", level+1)
            while n.next_p[level] != None and n.next_p[level].data < data:
                self.n_traverse +=1
                n = n.next_p[level]
            update[level] = n
            level -= 1
        return update
    
    def search_element(self,data,update=None):
        if update is None:
            update = self.update_vector(data)
        if len(update) > 0:
            element = update
            if element[0].next_p[0] != None and element[0].next_p[0].data == data:
                return element
        return None
    
    def insert_element(self,data, level=None):
        if level is None:
            level = self.random_level(self.max_level)
        if self.no_of_element == 0:
            new_node = Node(data,level)
            self.head = new_node
        else:
            new_node = Node(data,level)
            update = self.update_vector(data)
            if self.search_element(data,update) == None:
                for i in range(level):
                    new_node.next_p[i] = update[i].next_p[i]
                    update[i].next_p[i] = new_node
        self.no_of_element +=1
     
    def delete_element(self,data):
        """ deletion function taking care of deletion of max_level also."""
        if self.length == 0:
            raise ValueError("List is Empty")
        else:
            if self.search_element(data) == None:
                print("Data is not present in List")
            else:
                update = self.update_vector(data)
                current = update[0].next_p[0]
                if current != None and current.data == data:
                    for i in range(self.max_level-1):
                        if update[i].next_p[i] != current:
                            break
                        update[i].next_p[i] = current.next_p[i]
                else:
                    for i in range(self.max_level):
                        update[i].next_p[i] = None
                while(self.max_level >0 and self.head.next_p[self.max_level-1]==None):
                    self.max_level -= 1
        
def delete_element(skplst, data):
    if skplst.no_of_element == 0:
        raise ValueError("List is EMpty")
    else:
        update = skplst.update_vector(data)
        current = update[0].next_p[0]
        if update[0].next_p[0] != None and update[0].next_p[0].data == data:
            for i in range(skplst.max_level-1):
                if update[i].next_p[i] != current:
                    break
                update[i].next_p[i] = current.next_p[i]


def print_level(skiplst, level):
    print("level is ", level)
    node = skiplst.head
    while node:
        print("Data is =>",node.data)
        node = node.next_p[level]
    print("END",'\n')

if __name__ == "__main__":
    skplst = SkipList(5)
    for i in range(1,20,2):
        skplst.insert_element(i)
#    for i in range(1,20,2):
#        skplst.insert_element(i)
    skplst.insert_element(22)
    print_level(skplst,0)
    print_level(skplst,1)
    print_level(skplst,2)
    print_level(skplst,3)
        
        
        
