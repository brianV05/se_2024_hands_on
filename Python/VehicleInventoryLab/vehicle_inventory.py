from datetime import datetime
from enum import Enum


""" A program that solves real world problem using Python 
by applying the basics of common data structures and algorithms 
to solve business problems.
Author: [Your Name]
Course: Software Engineering Bootcamp
Date: [Date of last modification]
Name: Vehicle Inventory Management System
Description: A Python program that creates a vehicle inventory management system.
"""

class VehicleType(Enum):
    R = "Regular"
    E = "Electric"
    H = "Hybrid"


def formatItem(item, idx = 0):
    if idx == 0:
        return f"{str(item):< 10}"
    else:
        return "{:>10}".format(f"{str(item)}")
    
def mapVehcileType(vehicle_type):
    vehicle_type = vehicle_type.upper()
    if vehicle_type == "E":
        return VehicleType.E
    elif vehicle_type == "H":
        return VehicleType.H
    else:
        return VehicleType.R
    

    


# Base Class Fucntion
class Vehicle:
    """
    Initialize a Vehicle instance.
    """
    def __init__(self, stock_id, vin, year, make, model, odometer, sale_price, vehicle_type = VehicleType.R):
        self.stock_id  = stock_id
        self.vin = vin
        self.vechile_type = vehicle_type,
        self.year = year
        self.make = make
        self.model = model
        self.odometer = odometer
        self.sale_price = float(sale_price)

    def showDescription(self):
        """
        Display a formatted description of the vehicle's details.
        """
        items = [
            self.stock_id,
            self.vin,
            self.vehicle_type.value,
            self.year,
            self.make,
            self.model,
            self.odometer,
            self.sale_price
        ]

        if self.vechile_type == VehicleType.E:
            items.append(self.battery_size)
        else:
            items.append("")

        if self.vechile_type == VehicleType.H:
            items.append(self.mpg)
        else:
            items.append("")
        
        for idx, item in enumerate(items):
            print(formatItem(item, idx), end=" ")
        print("\n")




# HybridVechile Class
class HybridVehicle(Vehicle):
    """
    A class representing a Hybrid Vehicle (HV), inheriting from the Vehicle class.
    """
    def __init__(self, stock_id, vin, year, make, model, odometer, sale_price, mpg):
        super().__init__(stock_id, vin, year, make, model, odometer, sale_price, VehicleType.H)
        self.mpg = mpg

    def showDescription(self):
        super().showDescription()







