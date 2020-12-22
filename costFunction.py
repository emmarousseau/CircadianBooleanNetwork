


def costFunction(Model):
    
    total_cost = 0
    local_cost = 0
    cleared_edges = []
    for node in Model.network.nodes:
        local_cost = 0
        upstream_act = []
        downstream_act = []
        
        threshold_up = Model.parameters[node] 
        for real_value in Model.data[node]:
            if real_value >= threshold_up:
                upstream_act.append(1)
            else:
                upstream_act.append(0)
        
        for edge in node.outward:
             if edge not in cleared_edges:       
                delay = Model.parameters[edge]
                node2 = edge.node2
                threshold_down = Model.parameters[node2]
                if len(node2.inward) == 1:
                    for r_value in Model.data[node2]:
                        if r_value >= threshold_down:
                            downstream_act.append(1)
                        else:
                            downstream_act.append(0)
                    edgeType = Model.LC.gates[edge]
                    local_cost = correlation1on1(upstream_act, downstream_act, delay, edgeType)

                elif len(node2.inward) == 2:
                    other_up_node = node2.inward[0].node1
                    if (other_up_node == node):
                        other_up_node = node2.inward[1].node1
                        other_edge = node2.inward[1]
                    else:
                        other_edge = node2.inward[0]
                        cleared_edges.append(other_edge)
                    delay2 = Model.parameters[other_edge]
                    gate = Model.LC.gates[node2]
                    edgeType1 = Model.LC.gates[edge]
                    edgeType2 = Model.LC.gates[other_edge]
                    other_thres = Model.parameters[other_up_node]
                    other_node_act = []
                    for r_value in Model.data[other_up_node]:
                        if r_value >= other_thres:
                            other_node_act.append(1)
                        else:
                            other_node_act.append(0) 

                    local_cost = correlation2on1(upstream_act,other_node_act,downstream_act, gate, delay, delay2, edgeType1, edgeType2)

                

        total_cost += local_cost

    return total_cost

def correlation1on1(up, down, delay, edge):
    downstream_effect = []
    cost = 0
    for i in range(len(up)):
        downstream_effect.append(0)
    if edge == "INV":
        for i in range(len(up)):
            if up[i] == 0:
                downstream_effect[(i+delay)%16] = 1
    elif edge == "ID":
         for i in range(len(up)):
            if up[i] == 1:
                downstream_effect[(i+delay)%16] = 1

    for value1, value2 in zip(down,downstream_effect):
        if value1 == value2:
            cost += 1
    
    return cost

def correlation2on1(up1,up2,down, gate, delay1, delay2, edge1, edge2):
    
    downstream_effect = []
    for i in range(len(up1)):
        downstream_effect.append(0)
    cost = 0
    if gate == "AND":
        for i in range(len(downstream_effect)):
            if up1[(i-delay1)%16] == 1 and up2[(i-delay2)%16] == 1:
                downstream_effect[i] == 1
    elif gate == "OR":
        for i in range(len(downstream_effect)):
            if up1[(i-delay1)%16] == 1 or up2[(i-delay2)%16] == 1:
                    downstream_effect[i] == 1

    for value1, value2 in zip(down,downstream_effect):
        if value1 == value2:
            cost += 1

    return cost


        