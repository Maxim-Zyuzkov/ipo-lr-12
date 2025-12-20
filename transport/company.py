from transport.vehicle import Vehicle
from transport.client import Client

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []
    
    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Нужен транспорт")
        self.vehicles.append(vehicle)
        return True
    
    def list_vehicles(self):
        return self.vehicles.copy()
    
    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError("Нужен клиент")
        self.clients.append(client)
        return True
    
    def optimize_cargo_distribution(self):
        vip_clients = [c for c in self.clients if c.is_vip]
        regular_clients = [c for c in self.clients if not c.is_vip]
        all_clients = vip_clients + regular_clients
        
        results = {}
        
        for client in all_clients:
            loaded = False
            for vehicle in self.vehicles:
                if vehicle.get_free_space() >= client.cargo_weight:
                    if vehicle.load_cargo(client):
                        results[client.name] = vehicle.vehicle_id
                        loaded = True
                        break
            
            if not loaded:
                results[client.name] = "Не загружен"
        
        print(f"\nРаспределение грузов '{self.name}':")
        print("-" * 40)
        
        for client_name, vehicle_id in results.items():
            print(f"{client_name} -> {vehicle_id}")
        
        used_vehicles = [v for v in self.vehicles if v.current_load > 0]
        print(f"\nИспользовано транспорта: {len(used_vehicles)} из {len(self.vehicles)}")
        
        for vehicle in used_vehicles:
            print(f"\n{vehicle}")
            for client in vehicle.clients_list:
                print(f"  - {client.name} ({client.cargo_weight}т)")
        
        return results