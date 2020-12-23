
def costFunction(Model):
    
    total_cost = 0
    newcost1 = 0
    newcost2 = 0
    newcost3 = 0
    
    time = range(1,17)

    cry_act = []
    per_act = []
    bmal_act = []
    # edges: 0. bmal-cry 1. bmal-per 2. per-bmal 3. cry-bmal
    # nodes: 0. per 1. cry 2. bmal
    thres_cry = Model.parameters[Model.network.nodes[1]]
    thres_per = Model.parameters[Model.network.nodes[0]]
    thres_bmal = Model.parameters[Model.network.nodes[2]]
    signal_bmal_cry = Model.parameters[Model.network.edges[0]]
    signal_bmal_per = Model.parameters[Model.network.edges[1]]
    signal_per_bmal = Model.parameters[Model.network.edges[2]]
    signal_cry_bmal = Model.parameters[Model.network.edges[3]]

    for i in range(len(time)):
        cry_act.append(-1)
        per_act.append(-1)
        bmal_act.append(-1)

    if Model.data[Model.network.nodes[1]][0] >= thres_cry:
        cry_act[0] = 17
    else:
        cry_act[0] = 0

    if Model.data[Model.network.nodes[0]][0] >= thres_per:
        per_act[0] = 12
    else:
        per_act[0] = 0
    
    if Model.data[Model.network.nodes[2]][0] >= thres_bmal:
        bmal_act[0] = 3
    else:
        bmal_act[0] = 0

    LC = Model.LC.gates
    P_B = LC[Model.network.edges[2]]
    C_B = LC[Model.network.edges[3]]
    B_C = LC[Model.network.edges[0]]
    B_P = LC[Model.network.edges[1]]
    BMALgate = LC[Model.network.nodes[2]]

    for i in range(len(time)):
        for j in range(len(time)):
            if BMALgate == "AND":
                if P_B == "ID" and C_B == "ID":
                    if cry_act[(j-signal_cry_bmal)%16] == 17 and per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[j] = 3
                    elif cry_act[(j-signal_cry_bmal)%16] == 0 or per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[j] = 0
                elif P_B == "INV" and C_B == "ID":
                    if cry_act[(j-signal_cry_bmal)%16] == 0 and per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[j] = 3
                    elif cry_act[(j-signal_cry_bmal)%16] == 12 or per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[j] = 0
                elif P_B == "ID" and C_B == "INV":
                    if cry_act[(j-signal_cry_bmal)%16] == 17 and per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[j] = 3
                    elif cry_act[(j-signal_cry_bmal)%16] == 0 or per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[j] = 0
                elif P_B == "INV" and C_B == "INV":
                    if cry_act[(j-signal_cry_bmal)%16] == 0 and per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[j] = 3
                    elif cry_act[(j-signal_cry_bmal)%16] == 17 or per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[j] = 0
            elif BMALgate == "OR":
                if P_B == "ID" and C_B == "ID":
                    if cry_act[(j-signal_cry_bmal)%16] == 17 or per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[j] = 3
                    elif cry_act[(j-signal_cry_bmal)%16] == 0 and per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[j] = 0
                elif P_B == "INV" and C_B == "ID":
                    if cry_act[(j-signal_cry_bmal)%16] == 0 or per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[j] = 3
                    elif cry_act[(j-signal_cry_bmal)%16] == 17 and per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[j] = 0
                elif P_B == "ID" and C_B == "INV":
                    if cry_act[(j-signal_cry_bmal)%16] == 17 or per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[j] = 3
                    elif cry_act[(j-signal_cry_bmal)%16] == 0 and per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[j] = 0
                elif P_B == "INV" and C_B == "INV":
                    if cry_act[(j-signal_cry_bmal)%16] == 0 or per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[j] = 3
                    elif cry_act[(j-signal_cry_bmal)%16] == 17 and per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[j] = 0

            if B_C == "ID":
                if bmal_act[(j-signal_bmal_cry)%16] == 3:
                    cry_act[j] = 17
                elif bmal_act[(j-signal_bmal_cry)%16] == 0:
                   cry_act[j] = 0 
            elif B_C == "INV":
                if bmal_act[(j-signal_bmal_cry)%16] == 3:
                    cry_act[j] = 0
                elif bmal_act[(j-signal_bmal_cry)%16] == 0:
                   cry_act[j] = 17
            
            if B_P == "ID":
                if bmal_act[(j-signal_bmal_per)%16] == 3:
                    per_act[j] = 12
                elif bmal_act[(j-signal_bmal_per)%16] == 0:
                   per_act[j] = 0 
            elif B_P == "INV":
                if bmal_act[(j-signal_bmal_per)%16] == 3:
                    per_act[j] = 0
                elif bmal_act[(j-signal_bmal_per)%16] == 0:
                   per_act[j] = 12

    
    for value1, value2 in zip(Model.data[Model.network.nodes[1]], cry_act):
        newcost1 += abs(value1-value2)

    for value1, value2 in zip(Model.data[Model.network.nodes[0]], per_act):
        newcost2 += abs(value1-value2)

    for value1, value2 in zip(Model.data[Model.network.nodes[2]], bmal_act):
        newcost3 += abs(value1-value2)
    return cry_act, per_act, bmal_act, (newcost1+newcost2+newcost3)/3.0
