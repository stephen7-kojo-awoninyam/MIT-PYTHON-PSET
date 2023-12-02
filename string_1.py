import csv


class item:
    PayRate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity:int):
       
        assert price >= 0, f"{price} is not greater than zero"
        assert quantity >= 0, f"{quantity} is not greater than zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        item.all.append(self)
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv') as f:
            reader = csv.DictReader('f')
            Items = list(reader)
        for Item in Items:
            item(
                name = Item.get('name'),
                price = Item.get('price'),
                quantity = Item.get('quantity'), 
            )

    def calculate_total(self):
        return self.price * self.quantity  
    def apply_discount(self):
        self.price = self.price * item.PayRate  
        return self.price
    def __repr__(self) -> str:
        return f"item('{self.name}',{self.price},{self.quantity})"
        


item.instantiate_from_csv()

print(item.all)
        