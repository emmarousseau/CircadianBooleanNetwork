
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

    LC = Model.LC
    P_B = LC[0]
    C_B = LC[1]
    B_C = LC[2]
    B_P = LC[3]
    BMALgate = LC[5]

    for i in range(len(time)*2):
        for j in range(len(time)):
            if BMALgate == "AND":
                elif P_B == "ID" and C_B == "ID":
                    if cry_act[(j-signal_cry_bmal)%16] == 17 and per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[i] = 3
                    else:
                        bmal_act[i] = 0
                elif P_B == "INV" and C_B == "ID":
                    if cry_act[(j-signal_cry_bmal)%16] == 0 and per_act[(j-signal_per_bmal)%16] == 12:
                            bmal_act[i] = 3
                    else:
                        bmal_act[i] = 0
                elif P_B == "ID" and C_B == "INV":
                    if cry_act[(j-signal_cry_bmal)%16] == 17 and per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[i] = 3
                    else:
                        bmal_act[i] = 0
                elif P_B == "INV" and C_B == "INV":
                    if cry_act[(j-signal_cry_bmal)%16] == 0 and per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[i] = 3
                    else:
                        bmal_act[i] = 0
            elif BMALgate == "OR":
                if P_B == "ID" and C_B == "ID":
                    if cry_act[(j-signal_cry_bmal)%16] == 17 or per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[i] = 3
                    else:
                        bmal_act[i] = 0
                elif P_B == "INV" and C_B == "ID":
                    if cry_act[(j-signal_cry_bmal)%16] == 0 or per_act[(j-signal_per_bmal)%16] == 12:
                        bmal_act[i] = 3
                    else:
                        bmal_act[i] = 0
                elif P_B == "ID" and C_B == "INV":
                    if cry_act[(j-signal_cry_bmal)%16] == 17 or per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[i] = 3
                    else:
                        bmal_act[i] = 0
                elif P_B == "INV" and C_B == "INV":
                    if cry_act[(j-signal_cry_bmal)%16] == 0 or per_act[(j-signal_per_bmal)%16] == 0:
                        bmal_act[i] = 3
                    else:
                        bmal_act[i] = 0


            



    
    
    for value1, value2 in zip(Model.data[Model.network.nodes[1]], cry_act):
        newcost1 += abs(value1-value2)

    for value1, value2 in zip(Model.data[Model.network.nodes[0]], per_act):
        newcost2 += abs(value1-value2)

    return cry_act, per_act, (newcost1+newcost2)/2.0
