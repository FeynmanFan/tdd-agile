class LifeSupportSystem:
    def __init__(self):
        self.oxygen_level = 100

    def set_oxygen_level(self, level):
        self.oxygen_level = level

    def check_oxygen_level(self):
        if self.oxygen_level < 20:
            return f"Critical: Oxygen level at {self.oxygen_level}%"
        
        elif self.oxygen_level < 50:
            return f"Warning: Oxygen level at {self.oxygen_level}%"
        
        return f"Oxygen level stable at {self.oxygen_level}%"