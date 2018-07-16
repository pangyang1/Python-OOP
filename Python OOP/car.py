class Car(object):
    """docstring for Car."""
    def __init__(self,price,speed,fuel,mileage,tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax)


car1 =Car(2000,35,"Full",15,0.12)
car2 =Car(2000,5,"Not Full",105,0.12)
car3 =Car(2000,15,"Kind of Full",95,0.12)
car4 =Car(2000,25,"Full",25,0.12)
car5 =Car(2000,45,"Empty",25,0.12)
car6 =Car(20000000,35,"Empty",15,0.15)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
