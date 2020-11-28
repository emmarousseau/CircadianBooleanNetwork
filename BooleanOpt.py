# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:07:16 2020

@author: gogom
"""
import pandas as pd 
import numpy as np

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
        

def find_thres_var(ls):
    
    maxV = 0
    minV = 0
    for value in ls:
        if value > maxV:
            maxV = value
        if value < minV:
            minV =value
            
    valueRange = maxV - minV
    var = valueRange/10
    
    return (minV, var)

def find_all_comb(ls):
    
    minV, var = find_thres_var(ls)
    options = []
    for time in range(3,27,3):
        thresholds = (minV+i*var for i in range(0, 10))
        for thres in thresholds:
            options.append((time,thres))
            
    return options


data = pd.read_csv("transcriptome_matrix_mouse_liver.csv", sep=";")
data = data.iloc[[1,1213,45,686]]
data=data.drop(['BH.Q', 'ADJ.P', 'PER', 'LAG', 'AMP'], axis=1)
  
cry1 = list(data.iloc[0, 1:])
cry2 = list(data.iloc[1, 1:])
per1 = list(data.iloc[2, 1:])
per2 = list(data.iloc[3, 1:])

options = find_all_comb(cry1)
print(cry1)
