from Car import *


class Factory:

    @staticmethod
    def get_car(car_to_construct, car_type):
        if car_to_construct == "deportive":
            return DeportiveCar(car_type)
        elif car_to_construct == "family":
            return FamiliarCar(car_type)
        else:
            return "Not valid car to contruct"
