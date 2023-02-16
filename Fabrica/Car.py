class Car(object):
    def __init__(self, car_tipe) -> None:
        self.car_tipe = car_tipe
        self.status = 0 # 0 = turn down 1 = turn on

    def run(self):
        if self.status == 0:
            self.status = 1
        print("The car is ON")

    def shutDown(self):
        if self.status == 1:
            self.status = 0
        print("The car is off")

    def nitrus(self):
        print("High Speed NITRUS!!!!!")


class DeportiveCar(Car):
    def __init__(self, car_tipe) -> None:
        super(DeportiveCar, self).__init__(car_tipe)
        print("You Hav a Deportive car: ", self.car_tipe)


class FamiliarCar(Car):
    def __init__(self, car_tipe) -> None:
        super(FamiliarCar, self).__init__(car_tipe)
        print("You Hav a Family Car: ", self.car_tipe)

    def nitrus(self):
        print("The CAR NOT HAV  NITRUS :(")
