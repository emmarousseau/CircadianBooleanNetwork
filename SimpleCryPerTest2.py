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
import matplotlib.pyplot as plt

data = pd.read_csv("transcriptome_matrix_mouse_liver.csv", sep=";")
data = data.iloc[[1,1213,45,686]]
data=data.drop(['BH.Q', 'ADJ.P', 'PER', 'LAG', 'AMP'], 1)
  
cry1 = list(data.iloc[0, 1:])
cry2 = list(data.iloc[1, 1:])
per1 = list(data.iloc[2, 1:])
per2 = list(data.iloc[3, 1:])



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

time = range(1,17)

numbers = []
costs = []
all_models = []
for j in range(len(LCs)):

    a_LC = logCon.LC(Netw,LCs[j],chart, j)

    parameters = a_LC.possibleMODELS(data)
    models = []

    for model in parameters:
        new_model = mod.Model_OPT(a_LC, model, data) 
        models.append(new_model)
        all_models.append(new_model)

    for i in range(len(models)):
        numbers.append((j,i+1))
        decoy1, decoy2, model_cost = cost.costFunction(models[i])
        costs.append(model_cost)


good_fits = []
costs, all_models = (list(t) for t in zip(*sorted(zip(costs, all_models))))


number = 0
visIndex = numbers.index(numbers[number])
a_model = all_models[0]

print(a_model.LC.number)


plt.plot(time,cry1,c='tab:pink')
plt.plot(time,per1,c='tab:cyan')


cry_act, per_act, model_cost = cost.costFunction(a_model)
plt.plot(time,cry_act,c="r")
plt.plot(time,per_act,c="b")




plt.savefig("pts_graphs.png")
