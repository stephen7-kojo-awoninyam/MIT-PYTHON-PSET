class Item:
    pay_rate = 0.8

    all = []
    def __init__(self,name: str,price: int,quantity=0):

        assert quantity >= 0, f"Quantity of {quantity} should be greater than or equal to zero"
        assert price >= 0, f"price of {price} should be greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def discount(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f"item('{self.name}',{self.price},{self.quantity})"    
    



Item1 = Item("phone",5000,5)

Item1.discount()

print(Item1.price)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item1)
