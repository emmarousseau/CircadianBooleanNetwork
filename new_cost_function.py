
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
    signal_bmal-per = Model.parameters[Model.network.edges[1]]
    signal_per-bmal = Model.parameters[Model.network.edges[2]]
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


    if Model.LC.number == 0:
        for j in range(len(time)*2):
            for i in range(len(time)):
                if cry_act[i] == 17:
                    per_act[(i+signal_from_cry)%16] = 0
                elif cry_act[i] == 0:
                    per_act[(i+signal_from_cry)%16] = 12
                if per_act[i] == 12:
                    cry_act[(i+signal_from_per)%16] = 0
                elif per_act[i] == 0:
                    cry_act[(i+signal_from_per)%16] = 17

    elif Model.LC.number == 1:
        for j in range(len(time)*2):
            for i in range(len(time)):
                if cry_act[i] == 17:
                    per_act[(i+signal_from_cry)%16] = 12
                elif cry_act[i] == 0:
                    per_act[(i+signal_from_cry)%16] = 0
                if per_act[i] == 12:
                    cry_act[(i+signal_from_per)%16] = 0
                elif per_act[i] == 0:
                    cry_act[(i+signal_from_per)%16] = 17

    elif Model.LC.number == 2:
        for j in range(len(time)*2):
            for i in range(len(time)):
                if cry_act[i] == 17:
                    per_act[(i+signal_from_cry)%16] = 0
                elif cry_act[i] == 0:
                    per_act[(i+signal_from_cry)%16] = 12
                if per_act[i] == 12:
                    cry_act[(i+signal_from_per)%16] = 17
                elif per_act[i] == 0:
                    cry_act[(i+signal_from_per)%16] = 0

    elif Model.LC.number == 3:
        for j in range(len(time)*2):
            for i in range(len(time)):
                if cry_act[i] == 17:
                    per_act[(i+signal_from_cry)%16] = 12
                elif cry_act[i] == 0:
                    per_act[(i+signal_from_cry)%16] = 0
                if per_act[i] == 12:
                    cry_act[(i+signal_from_per)%16] = 17
                elif per_act[i] == 0:
                    cry_act[(i+signal_from_per)%16] = 0

    
    for value1, value2 in zip(Model.data[Model.network.nodes[1]], cry_act):
        newcost1 += abs(value1-value2)

    for value1, value2 in zip(Model.data[Model.network.nodes[0]], per_act):
        newcost2 += abs(value1-value2)

    return cry_act, per_act, (newcost1+newcost2)/2.0
