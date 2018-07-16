class Animal(object):
    """docstring of Animal."""
    def __init__(self, name, health):
        self.name = name
        self.health= health
    def walk(self):
        self.health -=1
        return self
    def run(self):
        self.health +=5
        return self
    def displayHealth(self):
        print self.health
        return self
class Dog(Animal):
    """docstring for Dog."""
    def __init__(self,name,health):
        super(Dog, self).__init__(name,health)
        self.health= health
    def pet(self):
        self.health +=5
        return self
    def displayHealth(self):
        print self.health

class Dragon(Animal):
    """docstring for Dragon."""
    def __init__(self,name, health):
        super(Dragon, self).__init__(name,health)
        self.health = health
    def fly(self):
        self.health -=10
        return self
    def displayHealth(self):
        print self.health
        print "I am a Dragon"



animal1 =Animal("Tito",200)
dog1 =Dog("Fido",150)
dragon1 =Dragon("Puff",170)

animal1.walk().walk().walk().run().run().displayHealth()
dog1.walk().walk().walk().run().run().pet().displayHealth()
dragon1.displayHealth()
