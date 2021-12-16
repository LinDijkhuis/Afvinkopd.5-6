class pet:

    def __init__(self, name, age, ani_type):
        self._name = name
        self._age = age
        self._type = ani_type

    def set__name(self, name):
        self.__name = name

    def get__name(self):
        return self.__name

    def set__animal_type(self, animal):
        self.__animal_type = animal

    def get__animal_type(self):
        return self.__animal_type

    def set__age(self, age):
        self.__age = age

    def get__age(self):
        return self.__age


if __name__ == '__main__':
    pets = pet("Sam", 6, "hoand")
    print("My pet is a", pets._type)
    print("The name of my pet is", pets._name)
    print("He is", pets._age, "years old")

    naam = input("Enter the name of your pet: ")
    pets.set__name(naam)
    age = input("How old is your pet?: ")
    pets.set__age(age)
    type = input("What kind of pet do you have?: ")
    pets.set__animal_type(type)
    print("Your pet is a:", pets.get__animal_type())
    print("The name of your pet:", pets.get__name())
    print("The age of your pet is:", pets.get__age())
