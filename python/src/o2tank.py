class o2tank:
    def __init__(self, initialLevel):
        self.internal_level = initialLevel

    @property
    def level(self):
        return self.internal_level
    
    @level.setter
    def level(self, value):
        self.internal_level = value