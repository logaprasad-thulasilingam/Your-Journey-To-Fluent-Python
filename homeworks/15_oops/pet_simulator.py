class Pet:
    def __init__(self, name, hunger, happiness, health):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.health = health

    def get_status(self):
        return f"Pet name is {self.name}, it is {self.hunger} & {self.happiness}. It's health is {self.health}"
    def feed(self):
        return f"{self.name} is eating"

    def play(self):
        self.happiness = "Happy"
        return f"{self.name} is {self.happiness}"


pet = Pet("Leo", "Hungry", "Sad", "Average")
print(pet.get_status())
print(pet.feed())
print(pet.play())