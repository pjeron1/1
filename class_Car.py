class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return "Рік", self.year,"Марка", self.make,"Модель", self.model



nisan = Car("nisan","gtr",2024)
audi = Car("audi","a7",2018)
jigul = Car("Jigul","Turbo 7000", 2077)

print(nisan.get_info())
print(audi.get_info())
print(jigul.get_info())