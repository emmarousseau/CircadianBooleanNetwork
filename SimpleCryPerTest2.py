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


Cry = node.Enzyme("Cry")
Per = node.Enzyme("Per")

Per_Cry = edge.Reaction(Per,Cry)
Cry_Per = edge.Reaction(Cry,Per)
Cry_Cry = edge.Reaction(Cry,Cry)


Netw = net.Network([Per,Cry],[Per_Cry,Cry_Cry,Cry_Per])

LCs, chart = Netw.possibleLCs()

print(LCs)
print(chart)

a_LC = logCon.LC(Netw,LCs[4],chart)
print(a_LC.gates)










