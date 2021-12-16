class Car:

    # Met init kun je je class variabele al vullen, (constructor)
    # Voordat je hem al gaat gebruiken. Als je hem aan maakt kun je
    # Als je de class aanmaakt kun je tussen de haakjes variabele
    # meegegeven. Set is om later aanpassen niet om te initialiseren.
    # Al vult voordat je bij je get komt, kun je geen get error krijgen.
    def __init__(self, model, make, speed):
        self.__model = model
        self.__make = make
        self.__speed = speed

    def set__year_model(self, model):
        self.__model = model

    def get__year_model(self):
        return self.__model

    def set__make(self, make):
        self.__make = make

    def get__make(self):
        return self.__make

    def set__speed(self, speed):
        self.__speed = speed

    def get__speed(self):
        return self.__speed

    def set__accelerate(self, attribute):
        self.__accelerate = attribute

    def get__accelerate(self):
        # Als deze wordt aangeroepen gaat die steeds sneller.
        self.__speed += 5
        # return self.__accelerate

    def set__brake(self, brake):
        self.__brake = brake

    def get__brake(self):
        # Hier wordt de snelheid vertraagd.
        self.__speed -= 5


if __name__ == '__main__':

    model = input("Enter the cars year model ")
    make = input("Enter the make of the car ")
    # Typeerror meestal string of integer of float.
    speed = int(input("Enter the cars current speed "))
    c1 = Car(model, make, speed)

    print(c1.get__year_model())
    print(c1.get__make())
    print(c1.get__speed())
    # Object ervoor, wil de speed printen (max. 5x). Moet weten
    # welk object. get speed is nog steeds een functie dus moet
    # De haakjes achter.

    print("Speeding up!")
    for i in range(5):
        c1.get__accelerate()
        print(c1.get__speed())

    print("Brake!")
    while c1.get__speed() != 30:
        c1.get__brake()
        print(c1.get__speed())
