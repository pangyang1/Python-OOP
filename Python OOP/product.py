class Product(object):
    """docstring for Product."""
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def status(self):
        if self.status == "defective":
            self.status = "defective"
            self.price = 0
        elif self.statue == "like new":
            self.status = "for sale"
        elif self.status == "opened":
            self.status = "used"
            self.price = (self.price*0.80)
        elif self.status == "sold":
            self.status = "sold"
        return self
    def tax(self):
        self.price = (self.price*0.10) + self.price
        return self
    def display_all(self):
        print "Price: " + str(self.price)
        print "Item: " + str(self.item_name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Status: " + str(self.status)


product1 =Product(100,"Shoes","5 lbs","Nike","defective")
product2 =Product(200,"Outfit","25 lbs","Gap","like new")
product3 =Product(300,"Necklace","1 lbs","Kay","opened")
product4 =Product(400,"Watch","2 lbs","Swiss","sold")

product1.tax().display_all()
product2.tax().display_all()
product3.tax().display_all()
product4.tax().display_all()
