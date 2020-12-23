

import NetworkClass as net
import ModelClass as mod
import LCClass as logCon
import EdgeClass as edge
import new_cost_function as cost
import NodeClass as node
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def isSimilar(original, test):
    count = 0
    for i,j in zip(original,test):
        if i==j:
            count += 1
    if count <3:
        return False
    else:
        return True

data = pd.read_csv("transcriptome_matrix_mouse_liver.csv", sep=";")
data = data.iloc[[1,1213,45,686]]
data=data.drop(['BH.Q', 'ADJ.P', 'PER', 'LAG', 'AMP'], 1)

prot_data = pd.read_csv("whole_proteome_mouse.csv", sep=";")
prot_data = prot_data.iloc[[668]]
prot_data= prot_data.drop(['GI', 'ID', 'Gene.Symbol', 'BH.Q', 'ADJ.P', 'PER', 'LAG', 'AMP'], 1)

bmal_act = [0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0]
cry_act = [17, 17, 0, 0, 0, 17, 17, 17, 17, 0, 0, 0, 0, 0, 17, 17]
per_act = [0, 0, 0, 12, 12, 12, 12, 0, 0, 0, 0, 0, 12, 12, 12, 12]

time = []
for t in range(16):
    time.append(t)

cry1 = list(data.iloc[0, 1:])
cry2 = list(data.iloc[1, 1:])
per1 = list(data.iloc[2, 1:])
per2 = list(data.iloc[3, 1:])
bmal = list(prot_data.iloc[0, 0:])

print(bmal)


plt.plot(time,bmal_act,c='g')
plt.plot(time,cry_act,c='b')
plt.plot(time,per_act,c='r')
plt.plot(time,bmal,c='g')
plt.plot(time,cry1,c='b')
plt.plot(time,per1,c='r')
plt.savefig("pts_graphs.png")


Cry = node.Enzyme("Cry")
Per = node.Enzyme("Per")
Bmal = node.Enzyme("Bmal")

data = {}
data[Cry] = cry1
data[Per] = per1
data[Bmal] = bmal

#Per_Cry = edge.Reaction(Per,Cry)
#Cry_Per = edge.Reaction(Cry,Per)
Bmal_Cry = edge.Reaction(Bmal, Cry)
Bmal_Per = edge.Reaction(Bmal, Per)
Per_Bmal = edge.Reaction(Per, Bmal)
Cry_Bmal = edge.Reaction(Cry, Bmal)

Netw = net.Network([Per,Cry, Bmal],[Bmal_Cry, Bmal_Per, Per_Bmal, Cry_Bmal])

"""
print(Netw.nodes)
print(Netw.edges)
print(len(bmal))
print(bmal)
"""

LCs, chart = Netw.possibleLCs()
original = [0,0,1,1,1]

"""
cleaned_LCs = []
for LC in LCs:
    if isSimilar(original,LC):
        cleaned_LCs.append(LC)
"""
cleaned_LCs = [original]

a_LC = logCon.LC(Netw,cleaned_LCs[0],chart, 0)
parameters = a_LC.possibleMODELS(data)

imp_costs = []
ref = []
bmal_list = []
cry_list = []
per_list = []
"""
print(cleaned_LCs[0])

for i in range(len(cleaned_LCs)):
    costs = []
    a_LC = logCon.LC(Netw,cleaned_LCs[i],chart, i)

    for par in range(len(parameters)):
        a_model = mod.Model_OPT(a_LC, parameters[par], data) 
        cry_now, per_now, bmal_now, a_cost = cost.costFunction(a_model)
        bmal_list.append(bmal_now)
        cry_list.append(cry_now)
        per_list.append(per_now)
        costs.append(a_cost)
        ref.append((i,par))
        print("Yeah!!! :", par)
    print("Bounga :", i)
    costs , ref = zip(*sorted(zip(costs, ref)))

    imp_costs.append(costs[0])
    print(ref[0])
    print(bmal_list[ref[0][1]])
    print(cry_list[ref[0][1]])
    print(per_list[ref[0][1]])
    




print(sorted(imp_costs))


"""

























    



