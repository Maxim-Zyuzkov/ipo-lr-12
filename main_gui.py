import dearpygui.dearpygui as dpg
from transport.client import Client
from transport.van import Van
from transport.ship import Ship
from transport.company import TransportCompany
import json

company = TransportCompany("Transport Company")

def add_client():
    with dpg.window(label="Add Client", modal=True, tag="win1"):
        dpg.add_text("Name:")
        n = dpg.add_input_text()
        dpg.add_text("Weight (t):")
        w = dpg.add_input_text()
        v = dpg.add_checkbox(label="VIP")
        
        def save():
            try:
                client = Client(dpg.get_value(n), float(dpg.get_value(w)), dpg.get_value(v))
                company.add_client(client)
                dpg.delete_item("win1")
            except: pass
        
        dpg.add_button(label="Save", callback=save)
        dpg.add_button(label="Cancel", callback=lambda: dpg.delete_item("win1"))

def add_vehicle():
    with dpg.window(label="Add Vehicle", modal=True, tag="win2"):
        t = dpg.add_combo(items=["Van", "Ship"])
        dpg.add_text("Capacity (t):")
        c = dpg.add_input_text()
        dpg.add_text("Name:")
        n = dpg.add_input_text()
        f = dpg.add_checkbox(label="Refrigerator")
        
        def save():
            try:
                typ = dpg.get_value(t)
                cap = float(dpg.get_value(c))
                name = dpg.get_value(n)
                fridge = dpg.get_value(f)
                
                if typ == "Van":
                    vehicle = Van(cap, fridge)
                else:
                    vehicle = Ship(cap, name)
                
                company.add_vehicle(vehicle)
                dpg.delete_item("win2")
            except: pass
        
        dpg.add_button(label="Save", callback=save)
        dpg.add_button(label="Cancel", callback=lambda: dpg.delete_item("win2"))

def optimize():
    try: company.optimize_cargo_distribution()
    except: pass

def export():
    try:
        data = {"clients": [], "vehicles": []}
        for c in company.clients:
            data["clients"].append({"name": c.name, "weight": c.cargo_weight, "vip": c.is_vip})
        for v in company.vehicles:
            if isinstance(v, Van):
                data["vehicles"].append({"type": "van", "id": v.vehicle_id, "capacity": v.capacity})
            elif isinstance(v, Ship):
                data["vehicles"].append({"type": "ship", "id": v.vehicle_id, "name": v.name, "capacity": v.capacity})
        with open("results.json", "w") as f:
            json.dump(data, f, indent=2)
    except: pass

def about():
    with dpg.window(label="About", modal=True, tag="win3"):
        dpg.add_text("Lab 13")
        dpg.add_text("Variant 3")
        dpg.add_text("Student: Fakaly Saveliy")
        dpg.add_text("Group: 89TP")
        dpg.add_text("CYRILLIC IS NOT SUPPORTED")
        dpg.add_button(label="Close", callback=lambda: dpg.delete_item("win3"))

def main():
    dpg.create_context()
    
    dpg.create_viewport(title='Transport Logistics', width=600, height=400)
    
    with dpg.window(label="Main Window", width=600, height=400):
        dpg.add_button(label="Add Client", callback=add_client)
        dpg.add_button(label="Add Vehicle", callback=add_vehicle)
        dpg.add_button(label="Optimize", callback=optimize)
        dpg.add_button(label="Export JSON", callback=export)
        dpg.add_button(label="About", callback=about)
    
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()