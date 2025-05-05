class ShoppingCart:

    def add_item(self, age, count):
        self.age = age
        self.count = count
        self.boolI = True
        print(f"{self.age}, {self.count}, {self.boolI}")

obj1: ShoppingCart = ShoppingCart()
obj2: ShoppingCart = ShoppingCart()
obj2.boolI = False

obj1.add_item(20, 1)
obj2.add_item(20, 1)


