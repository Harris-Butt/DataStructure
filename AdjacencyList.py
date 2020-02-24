# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:22:16 2020

@author: workbook
"""

class Vertex:
    def __init__(self,name):
        self.name = name
        self.neighbors = []
    def add_neighbor(self,vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()
class Graph:
    vertices = {}
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
        
        
            