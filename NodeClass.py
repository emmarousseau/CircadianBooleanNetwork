

class Enzyme:
    
    def __init__(self, name):
        
        self.name = name
        self.threshold = None
        self.inward = []
        self.outward = []
        self.gate = None
