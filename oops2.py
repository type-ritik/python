class Person:
    number_of_peoples = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return cls.number_of_peoples

    @classmethod
    def add_person(cls):
        cls.number_of_peoples += 1


p1 = Person("Mike")
p2 = Person("Billy")
p3 = Person("Kelly")

print(Person.number_of_people())
