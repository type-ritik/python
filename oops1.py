# Inheritance


# Generalization
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print(f"I don't know what I say")


# I am inheriting the proerties of Pet or Upper level class
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")


class Dog(Pet):
    # Method
    def speak(self):
        print("bark")


class Fish(Pet):
    pass


p = Pet("Time", 19)
p.show()
p.speak()

cat1 = Cat("Bill", 26, "Red")
cat1.show()
cat1.speak()

dog1 = Dog("John", 25)
dog1.show()
dog1.speak()


fish1 = Fish("Mit", 10)
fish1.show()
fish1.speak()
