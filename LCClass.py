

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
        for edge in self.network.edges:
            delays[edge] = new_ls
        name_list = []
        values_lists = []
        models = []
        numb_models = 1

        for k,v in thresholds.items():
            name_list.append(k)
            values_lists.append(v)
            numb_models *= len(v)

        for k,v in delays.items():
            name_list.append(k)
            values_lists.append(v)
            numb_models *= len(v)

        all_comb = list(itert.product(*values_lists))

        for comb in all_comb:
            new_dict = {}
            for name in len(name_list):
                new_dict[name_list[name]] = comb[name]
            models.append(new_dict)

        return models
