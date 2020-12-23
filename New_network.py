

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
Bmal = node.Enzyme("Bmal")

data = {}
data[Cry] = cry1
data[Per] = per1
data[Bmal] = bmal

Per_Cry = edge.Reaction(Per,Cry)
Cry_Per = edge.Reaction(Cry,Per)
Bmal_Cry = edge.Reaction(Bmal, Cry)
Bmal_Per = edge.Reaction(Bmal, Per)
Per_Bmal = edge.Reaction(Per, Bmal)
Cry_Bmal = edge.Reaction(Cry, Bmal)

Netw = net.Network([Per,Cry, Bmal],[Per_Cry,Cry_Per, Bmal_Cry, Bmal_Per, Per_Bmal, Cry_Bmal])

print(Netw.nodes)
print(Netw.edges)

LCs, chart = Netw.possibleLCs()

    



