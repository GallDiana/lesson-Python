class Human:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.iq = 1


class Auto:

    def __init__(self,brand,model,color):
        self.brand = brand
        self.model= model
        self.color = color
        self.passanger = []

    def add_passanger(self,*args):
        for passenger in args:
            self.passanger.append(passenger)

    def print_passenger(self):
        if self.passanger != []:
            print(f"Names of {self.brand}  {self.model} passenger")

            for passenger in self.passanger:
                print(passenger.name)

        else:
            print(f"There are no passenger in {self.brand} {self.model}")

diana = Human("Diana",12)
anna = Human("Anna",12)

zhiguli_7 = Auto("lada","2107","cherry")

zhiguli_7.add_passanger(diana,anna)

zhiguli_7.print_passenger()
