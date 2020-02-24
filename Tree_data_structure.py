# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:46:39 2020

@author: workbook
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.rightChild = None
        self.leftChild  = None
    def insert(self,value):
        #check duplicate value
        if value == self.value:
            return False
        #if value is less than current node 
        #insert value left
        if value < self.value:
            if self.leftChild:
                return self.leftChild.insert(value)
            else:
                self.leftChild = Node(value)
                return True
        #if value is greater than current node
        #insert value right
        if value > self.value:
            if self.rightChild:
                return self.rightChild.insert(value)
            else:
                self.rightChild = Node(value)
                return True
    def find(self,value):
        # if value is equal to the value at current node
        if value == self.value:
            return True
        # if value is less than the value at current node
        elif value<self.value:
            if self.leftChild:
                self.leftChild.find(value)
            else:
                return False
            
        # if value is greater than the value at current node
        elif value > self.value:
            if self.rightChild:
                self.rightChild.find(value)
            else:
                return False
    def preOrder(self):
        if self:
            print(self.value)
            if self.leftChild:
                self.leftChild.preOrder()
            
            if self.rightChild:
                self.rightChild.preOrder()
    def postOrder(self):
        if self:
            if self.leftChild:
                self.leftChild.postOrder()
            if self.rightChild:
                self.rightChild.postOrder()
            print(self.value)
    def inOrder(self):
        if self:
            if self.leftChild:
                self.leftChild.inOrder()
            print(self.value)
            
            if self.rightChild:
                self.rightChild.inOrder()
            
            
            
            
        
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        #insert in root
        if self.root is None:
            self.root = Node(value)
            return True
        else:
            self.root.insert(value)
    #find value in a tree
    def find(self,value):
        if self.root is None:
            return False
        else:
            return self.root.find(value)
    def preOrder(self):
        self.root.preorder()
    def postOrder(self):
        self.root.postOrder()
    def inOrder(self):
        self.root.inOrder()
        
        