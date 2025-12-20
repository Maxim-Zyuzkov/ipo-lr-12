# 3 вариант

from transport.client import Client
from transport.van import Van
from transport.ship import Ship
from transport.company import TransportCompany

def main():
    print("=" * 50)
    print("СИСТЕМА ТРАНСПОРТНОЙ ЛОГИСТИКИ")
    print("=" * 50)
    
    company_name = input("Название компании: ")
    company = TransportCompany(company_name)
    
    while True:
        print("\nМЕНЮ:")
        print("1. Добавить клиента")
        print("2. Добавить транспорт")
        print("3. Показать клиентов")
        print("4. Показать транспорт")
        print("5. Распределить грузы")
        print("6. Выход")
        
        choice = input("Выберите (1-6): ")
        
        if choice == "1":
            try:
                name = input("Имя клиента: ")
                weight = float(input("Вес груза (т): "))
                vip = input("VIP? (да/нет): ").lower() in ["да", "yes", "y", "1"]
                
                client = Client(name, weight, vip)
                company.add_client(client)
                print(f"Клиент '{name}' добавлен")
            except Exception as e:
                print(f"Ошибка: {e}")
        
        elif choice == "2":
            print("1. Фургон")
            print("2. Судно")
            type_choice = input("Тип (1-2): ")
            
            try:
                capacity = float(input("Грузоподъемность (т): "))
                
                if type_choice == "1":
                    fridge = input("Холодильник? (да/нет): ").lower() in ["да", "yes", "y", "1"]
                    vehicle = Van(capacity, fridge)
                    print(f"Фургон добавлен. ID: {vehicle.vehicle_id}")
                
                elif type_choice == "2":
                    name = input("Название судна: ")
                    vehicle = Ship(capacity, name)
                    print(f"Судно '{name}' добавлено. ID: {vehicle.vehicle_id}")
                
                else:
                    print("Неверный выбор")
                    continue
                
                company.add_vehicle(vehicle)
                
            except Exception as e:
                print(f"Ошибка: {e}")
        
        elif choice == "3":
            print("\nКЛИЕНТЫ:")
            if not company.clients:
                print("Нет клиентов")
            else:
                for i, client in enumerate(company.clients, 1):
                    print(f"{i}. {client}")
        
        elif choice == "4":
            print("\nТРАНСПОРТ:")
            if not company.vehicles:
                print("Нет транспорта")
            else:
                for i, vehicle in enumerate(company.vehicles, 1):
                    print(f"{i}. {vehicle}")
        
        elif choice == "5":
            company.optimize_cargo_distribution()
        
        elif choice == "6":
            print("Выход")
            break
        
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()