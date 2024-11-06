class Vehicle:
    def __init__(self, make, model, year, tank_capacity, engine_consumption, engine_hp):
        self.make = make
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.engine_consumption = engine_consumption
        self.engine_hp = engine_hp

    def mileage_(self, loss_coeficient):
        return (self.tank_capacity * 100) / self.engine_consumption * loss_coeficient

    def towing_capacity_(self, vehicle_coeficient):
        return self.tank_capacity * self.engine_hp * vehicle_coeficient
    
    def print_vehicle(self):
        print("Vehicle:")
        print("\tmake:", self.make)
        print("\tmodel:", self.model)
        print("\tyear:", self.year)
        print("\ttank_capacity:", self.tank_capacity)
        print("\tengine_consumption:", self.engine_consumption)
        print("\tengine_hp:", self.engine_hp)


class Car(Vehicle):
    def __init__(self, make, model, year, tank_capacity, engine_consumption, engine_hp):
        super().__init__(make, model, year, tank_capacity, engine_consumption, engine_hp)

    def mileage(self):
        return self.mileage_(0.80)

    def towing_capacity(self):
        return self.towing_capacity_(0.6)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, tank_capacity, engine_consumption, engine_hp):
        super().__init__(make, model, year, tank_capacity, engine_consumption, engine_hp)

    def mileage(self):
        return self.mileage_(0.85)

    def towing_capacity(self):
        return self.towing_capacity_(0.1)


class Truck(Vehicle):
    def __init__(self, make, model, year, tank_capacity, engine_consumption, engine_hp):
        super().__init__(make, model, year, tank_capacity, engine_consumption, engine_hp)

    def mileage(self):
        return self.mileage_(0.70)

    def towing_capacity(self):
        return self.towing_capacity_(0.95)


vehicles = [
    Car("Ford", "Focus", 2023, 50, 6, 150),
    Motorcycle("Harley", "Sportster", 2020, 12, 4, 70),
    Truck("Volvo", "FH16", 2019, 400, 25, 550),
    Car("Toyota", "Corolla", 2021, 55, 6.5, 130),
    Motorcycle("Yamaha", "MT-07", 2022, 14, 5, 75),
    Truck("Scania", "R 500", 2018, 500, 18, 650),
]

for vehicle in vehicles:
    vehicle.print_vehicle()
    print("vehicle mileage:", vehicle.mileage(), "km")
    print("vehicle towing capacity:", vehicle.towing_capacity(), "hp")
    print()
