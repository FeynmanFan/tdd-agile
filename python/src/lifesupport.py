class LifeSupportSystem:
    def __init__(self, isActive=False):
        self.oxygen_level = 100
        self.isActive = isActive

    def set_oxygen_level(self, level):
        self.oxygen_level = level

    def check_oxygen_level(self):
        if self.oxygen_level < 20:
            self.oxygen_level = 80
            return "Oxygen replenished to 80%"
        
        elif self.oxygen_level < 50:
            return f"Warning: Oxygen level at {self.oxygen_level}%"
        
        return f"Oxygen level stable at {self.oxygen_level}%"