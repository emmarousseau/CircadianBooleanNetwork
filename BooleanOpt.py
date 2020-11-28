# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:07:16 2020

@author: gogom
"""
import pandas as pd

class Edge:
    
    def __init__(self, signal_delay):
        
        self.delay = signal_delay
        
        
class Node:
    
    def __init_(self, threshold):
        
        self.threshold = threshold
        

data = pd.read_csv("https://github.com/emmarousseau/CircadianBooleanNetwork/blob/main/transcriptome_matrix_mouse_liver.csv", error_bad_lines=False)
print(data.head())