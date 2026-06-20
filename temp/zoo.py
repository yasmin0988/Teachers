class Animal:
    def __init__(self, name=str, specie=str, age=int, sound=str, zoo_name=str):
        self.name = name
        self.specie = specie
        self.age = age
        self.sound = sound
        self.zoo_name=zoo_name
    
    def make_sound(self):
        print(self.sound)

    def info(self):
        print(f"name: {self.name}")
        print(f"specie: {self.specie}")
        print(f"age: {self.age}")
        print(f"sound: {self.sound}")
        print(f"zoo_name: {self.zoo_name}")

    def __str__(self):
        data = f"{self.name}, {self.specie}, {self.age}, {self.sound}, {self.zoo_name}"
        print(data)
        

class Bird(Animal):
    def __init__(self, name=str, specie=str, age=int, sound=str, zoo_name=str, wing_span=float):
        Animal.__init__(name, specie, age, sound, zoo_name)
        self.wing_span = wing_span

    def make_sound(self):
        print(self.sound)



lion = Animal("lion", "cats", 5, "roar", "bla")
lion.info()
lion.make_sound()
lion.__str__()
chicken = Bird("hen", "red junglefowl", 2, "jik", "blabla", 10.5)
chicken.info()
chicken.make_sound()
chicken.__str__()