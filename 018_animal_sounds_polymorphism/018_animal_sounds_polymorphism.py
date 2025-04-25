class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"

def animal_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()
cow = Cow()

print("Dog says:", animal_sound(dog))
print("Cat says:", animal_sound(cat))
print("Cow says:", animal_sound(cow))
