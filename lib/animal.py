class Animal:
    def __init__(self,species,food,sound):
        self.species=species
        self.food=food
        self.sound=sound
    def animal_attributes(self):
        return f'The {self.species},eats {self.food} and! {self.sound}'
        
    def move(self):
        return 'and yes all the animals can move'
    #instances
lion =Animal('lion',"meat",'roars')
dog=Animal('dog:', 'meat','barks')
cat=Animal('cat','milk','meow!')

print(lion.animal_attributes())
print(dog.animal_attributes())
print(lion.move())