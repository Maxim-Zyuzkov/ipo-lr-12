from transport.vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, capacity, is_refrigerated=False):
        super().__init__(capacity)
        self.is_refrigerated = bool(is_refrigerated)
    
    def __str__(self):
        fridge = "с холодильником" if self.is_refrigerated else "без холодильника"
        return f"Фургон {fridge}, " + super().__str__()