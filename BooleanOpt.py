# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:07:16 2020

@author: gogom

"""
import pandas as pd

class Edge:
    
    def __init__(self, signal_delay, start, end, function):
        
        self.delay = signal_delay
        self. start = start
        self.end = end
        self.function = function
        
        
class Node:
    
    def __init_(self, threshold, entering, exiting):
        
        self.threshold = threshold
        self.entering_edges = []
        self.exiting_edges = []
        


        for edge in entering:
            self.entering_edges.append(edge)
            
        for edge in exiting:
            self.exiting_edges.append(edge)


data = pd.read_csv("transcriptome_matrix_mouse_liver.csv", error_bad_lines=False)
cry1_data = data.iloc[1,0]

print(type(cry1_data))