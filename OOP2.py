class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, qty: int, unit_price: float):
        # Do the explanation here.....#
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):

        for j in self.items:
            if j[0] == item_name:
                self.items.remove(j)
                break

    def calculate_total(self) -> float:
        total = 0.0

        for name, qty, price in self.items:
            total += qty * price

        return total

    def summary(self):

        print("Cart Contents")

        for name, qty, price in self.items:
            print(f"{name}: {qty} @ Ksh{price}:.3f each")
        print(f"Total: Ksh {self.calculate_total()}:.2f\n")

def checkout(cart: ShoppingCart):
        cart.summary()
        print(f"Final amount: Ksh {cart.calculate_total()}\n")



#Usage
if __name__ == "__main__":

    cart: ShoppingCart = ShoppingCart()
    cart.add_item("Kiwi", 50, 70.2)
    cart.add_item("Papaya", 30, 40.3)
    cart.add_item("Guava", 10, 20.1)
    cart.add_item("Mango", 40, 50.5)

    print(">>> Regular Cart <<<")

    checkout(cart)
