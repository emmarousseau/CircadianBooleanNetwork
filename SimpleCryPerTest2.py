# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:36:00 2020

@author: gogom
"""

import NetworkClass as net
import ModelClass as mod
import LCClass as logCon
import EdgeClass as edge
import costFunction as cost
import NodeClass as node
import pandas as pd 
import numpy as np

data = pd.read_csv("transcriptome_matrix_mouse_liver.csv", sep=";")
data = data.iloc[[1,1213,45,686]]
data=data.drop(['BH.Q', 'ADJ.P', 'PER', 'LAG', 'AMP'], 1)
  
cry1 = list(data.iloc[0, 1:])
cry2 = list(data.iloc[1, 1:])
per1 = list(data.iloc[2, 1:])
per2 = list(data.iloc[3, 1:])

#print(cry1)
#print(per1)

Cry = node.Enzyme("Cry")
Per = node.Enzyme("Per")

Per_Cry = edge.Reaction(Per,Cry)
Cry_Per = edge.Reaction(Cry,Per)


Netw = net.Network([Per,Cry],[Per_Cry,Cry_Per])

LCs, chart = Netw.possibleLCs()

#print("LCs : ", LCs)
#print("chart : ", chart)

#a_LC = logCon.LC(Netw,LCs[15],chart)
#print("one gate : ", a_LC.gates)

data = {}

data[Cry] = cry1
data[Per] = per1


#print("models : ", models[100000])

"""
a_model = mod.Model_OPT(a_LC, models[], data)
#print(a_model.LC.gates)

a_cost = cost.costFunction(a_model)
print(a_cost)

"""
numbers = []
costs = []
for j in range(len(LCs)):

    a_LC = logCon.LC(Netw,LCs[j],chart)

    parameters = a_LC.possibleMODELS(data)
    models = []

    for model in parameters:
        new_model = mod.Model_OPT(a_LC, model, data)
        models.append(new_model)

    for i in range(len(models)):
        numbers.append((j,i+1))
        costs.append(cost.costFunction(models[i]))



print(max(costs))

print(costs)













