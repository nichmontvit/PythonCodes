class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        pass
    
    def __str__(self):
        return "Current floor: {}".format(self.current)
        pass
    
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current >= 10:
            self.current = self.top
        else:
            self.current = self.current + 1
        self.current
        pass
    
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current < -1:
            self.current = self.bottom
        else:
            self.current = self.current - 1
        self.current
        pass
    
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        self.current
        pass

elevator = Elevator(-1, 10, 0)