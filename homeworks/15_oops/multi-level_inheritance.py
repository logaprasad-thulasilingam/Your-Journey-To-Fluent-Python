class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} is eating"

class Mammal(Animal):
    def __init__(self,name,has_fur):
        super().__init__(name)
        self.has_fur = has_fur
    def walk(self):
        return f"{self.name} is walking"

class Dog(Mammal):
    def __init__(self,name,has_fur,breed):
        super().__init__(name,has_fur)
        self.breed = breed
    def bark(self):
        return f"{self.name} can Bark"
    def fur_info(self):
        if self.has_fur == True:
            return f"{self.name} is having fur"
        else:
            return f"{self.name} does not have fur"

class Cat(Mammal):
    def __init__(self, name, has_fur, breed):
        Mammal.__init__(self,name,has_fur)
        self.breed = breed
    def meow(self):
        return f"{self.name} can meow"


if __name__ == '__main__':
    a = Dog(name="Leo", has_fur=True, breed="Labrador")
    print(a.walk(), '\n', a.bark())
    print (a.fur_info())

    b = Cat(name="Min", has_fur=False, breed="Persian")
    print(b.walk(), '\n', b.meow())
