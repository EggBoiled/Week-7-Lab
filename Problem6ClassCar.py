#Modifying a the code to add attributes of types and manufacturer

class car:

    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_color(self):
        return self.color
    def  get_type(self):
        return self.type
    def get_manufacturer(self):
        return self.manufacturer
    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type + ' ' + self.manufacturer
car1 = car("sports", 2012, "blue", "honda", "SUV")
car2 = car("sedan", 2020, "black", "Toyota", "VAN")

print(car1.get_color())
print(car1.get_model())
print(car1.get_type())
print(car1.get_manufacturer())
print(car2.get_color())
print(car2.get_model())
print(car2.get_type())
print(car2.get_manufacturer())
print(car1.fullspecs())
print(car2.fullspecs())