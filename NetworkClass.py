# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:00:06 2020

@author: gogom
"""

import math 
import itertools as itert

#Object representing the nodes of the network

class Enzyme:
    
    def __init__(self, name):
        
        self.name = name
        self.threshold = None
        self.inward = []
        self.outward = []
        self.gate = None

#Object representing the edges of the network

class Reaction:
    
    def __init__(self, node1, node2):
        
        self.node1 = node1
        self.node2 = node2
        node1.outward.append(self)
        node2.inward.append(self)
        self.action = None
        self.delay = None

class LC:
    
    def __init__(self, network, gates, chart):
        
        self.gates = {}
        self.network = network
        self.chart = chart
        
        abs_count = 0

        for node in network.nodes:
            self.gates[node] = None

        for elem in chart:
            for sub_elem in elem:
                
                if sub_elem == 'gate':
                    if gates[abs_count] == 1:
                        self.gates[elem[elem.index(sub_elem)-1].node2] = "AND"
                    elif gates[abs_count] == 0:
                        self.gates[elem[elem.index(sub_elem)-1].node2] = "OR"
                        
                else:
                    if gates[abs_count] == 1:
                        self.gates[sub_elem] = "ID"
                    elif gates[abs_count] == 0:
                        self.gates[sub_elem] = "INV"
                abs_count += 1
        
    def possibleMODELS(self, data):
        thresholds = {}
            
        for node in self.network.nodes:
            unique_values = set(data[node])
            new_list = []
            for elem in unique_values:
                new_list.append(elem)
            thresholds[node] = new_list

        new_ls = []        
        for i in range(1,9):
            new_ls.append(i) 
        
                
        delays = {}
        for edge in network.edges:
            delays[edge] = new_ls
        name_list = []
        values_lists = []
        models = []
        numb_models = 1

        for k,v in threshold.items():
            name_list.append(k)
            lists.append(v)
            numb_models *= len(v)

        for k,v in delays.items():
            name_list.append(k)
            lists.append(v)
            numb_models *= len(v)

        all_comb = list(itert.product(*values_lists))

        for comb in all_comb:
            new_dict = {}
            for name in len(name_list):
                new_dict[name_list[name]] = comb[name]
            models.append(new_dict)

        return models

            

        
class Model_OPT:
    
    def __init__(self, LC, parameters, data):
        self.LC = LC
        self.parameters = parameters
        self.network = self.LC.network
        
        
class Network:
    
    def __init__(self, list_nodes, list_edges):
        
        self.nodes = list_nodes
        self.edges = list_edges
        
        
    def addNode(self, node):
        self.nodes.append(node)
        
        
    def addEdge(self, edge):
        self.edges.append(edge)
        
    def possibleLCs(self):
        
        LCs = []
        chart = []

        count = 0
        for node in self.nodes:
            if len(node.inward) == 1:
                count += 1
            elif len(node.inward) == 2:
                count += 3
                
        nodes = self.nodes
        
        for i in range(2**count):
            LCs.append(binaryList(i,count))
            
            
        for node in self.nodes:
            if len(node.inward) == 1:
                chart.append((node.inward[0],))
            if len(node.inward) == 2:
                chart.append((node.inward[0],
                              node.inward[1],
                              "gate"))
                
        return (LCs, chart)

    #AND and ID are 1, OR and NOT are 0 !!!!!!!!
        
        
        
def costFunction(Model, data):
    
    total_cost = 0
    local_cost = 0
    cleared_edges = []
    for node in Model.network.nodes:
        local_cost = 0
        upstream_act = []
        downstream_act = []
        
        threshold_up = Model[node] 
        for real_value in data[node]:
            if real_value <= threshold_up:
                upstream_act.append(1)
            else:
                upstream_act.append(0)
        
        for edge in node.outward:
             if edge not in cleared_edges:       
                delay = Model[edge]
                node2 = edge.node2
                threshold_down = Model[node2]
                if len(node2.inward) == 1:
                    for r_value in data[node2]:
                        if r_value <= threshold_down:
                            downstream_act.append(1)
                        else:
                            downstream_act.append(0)
                    local_cost = correlation1on1(upstream_act, downstream_act, delay)

                elif len(node2.inward) == 2:
                    other_up_node = node2.inward[0].node1
                    other_edge = node2.inward[0]
                    if (other_up_node == node):
                        other_up_node = node2.inward[1].node1
                        other_edge = node2.inward[1]
                    delay2 = Model[other_edge]
                    gate = Model.LC[node2]
                    other_thres = Model[other_up]
                    other_node_act = []
                    for r_value in data[other_up_node]:
                        if r_value <= other_thres:
                            other_node_act.append(1)
                        else:
                            other_node_act.append(0) 

                    local_cost = correlation2on1(upstream_act,other_node_act,downstream_act, gate, delay, delay2)

                

        total_cost += local_cost

    return total_cost

def correlation1on1(up, down, delay):
    downstream_effect = []
    cost = 0
    for i in len(up):
        downstream_effet.append(0)
    for i in len(up):
        if up[i] == 1:
            downstream_effect[(i+delay)%16] = 1

    for value1, value2 in zip(down,downstream_effect):
        if value1 == value2:
            cost += 1
    
    return cost

def correlation2on1(up1,up2,down, gate, delay1, delay2):
    
    downstream_effect = []
    for i in len(up1):
        downstream_effect.append(0)
    cost = 0
    if gate == "AND":
        for i in len(downstream_effect):
            if up1[(i-delay1)%16] == 1 and up2[(i-delay2)%16] == 1:
                downstream_effect[i] == 1
    elif gate == "OR":
        if up1[(i-delay1)%16] == 1 or up2[(i-delay2)%16] == 1:
                downstream_effect[i] == 1

    for value1, value2 in zip(down,downstream_effect):
        if value1 == value2:
            cost += 1

    return cost

def binaryList(numb, size):
    number = []
    for i in range(size):
        number.append(0)
            
    for i in range(numb):
        for j in range(size):
            if number[j] == 0:
                number[j] = 1
                break
            elif number[j] == 1:
                number[j] = 0
                continue
                
    return number
        
           
if __name__ == "__main__":
    numb = binaryList(6,4)
    print(numb)

    
    