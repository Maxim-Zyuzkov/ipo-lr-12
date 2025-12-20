from transport.vehicle import Vehicle

class Ship(Vehicle):
    def __init__(self, capacity, name):
        super().__init__(capacity)
        if not name or not isinstance(name, str):
            raise ValueError("Нужно название судна")
        self.name = name
    
    def __str__(self):
        return f"Судно '{self.name}', " + super().__str__()