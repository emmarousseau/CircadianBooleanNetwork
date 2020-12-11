

class Reaction:
    
    def __init__(self, node1, node2):
        
        self.node1 = node1
        self.node2 = node2
        node1.outward.append(self)
        node2.inward.append(self)
        self.action = None
        self.delay = None