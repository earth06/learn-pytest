class Configure:

    def __init__(self,cfg, params):
        self.cfg = cfg
        self.params = params
    
    def get_configA(self):
        return self.cfg["A"]