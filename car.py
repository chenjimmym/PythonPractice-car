class car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayAll()

    def displayAll(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        print "-----------------"

car1 = car(2000,"35mph", "Full", "15mpg")
car2 = car(2000,"5mph", "Not Full", "105mpg")
car3 = car(2000,"15mph", "Kind of Full", "95mpg")
car4 = car(2000,"25mph", "Full", "25mpg")
car5 = car(2000,"45mph", "Empty", "25mpg")
car6 = car(20000000,"35mph", "Empty", "15mpg")