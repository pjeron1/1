class Plant:
    def __init__(self, name):
        self.name = name




class Fruit:
    def __init__(self, sweet_or_salty):
        self.sweet_or_salty = sweet_or_salty

    def fruit(self):
        print(f"Рослина з {self.sweet_or_salty} плодами ")

class Fruittree(Plant, Fruit):
    def __init__(self, name, sweet_or_salty):
        super().__init__(sweet_or_salty)
        Plant.__init__(self, name)




fruit_tree1 = Fruittree(name="Яблуня", sweet_or_salty="Солодка")
print(fruit_tree1.name)

