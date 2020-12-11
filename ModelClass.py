

class Model_OPT:
    
    def __init__(self, LC, parameters, data):
        self.LC = LC
        self.parameters = parameters
        self.network = self.LC.network
        
        