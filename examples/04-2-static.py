# from typing import List


class Category:
    SALE = 200
    name: str
    products: list

    def __init__(self, category_name: str):
        self.name = category_name
        self.products = []

    def add_product(self, item):
        self.products.append(item)

    def get_count(self):
        return len(self.products)

    def get_total_cost(self):
        sum = 0

        for item in self.products:
            sum += item.price

        return sum

    @classmethod
    def total_with_sale(cls, value):
        return value - cls.SALE


class Product:
    name: str
    price: int

    def __init__(self, item_name: str, item_price: int):
        self.name = item_name
        self.price = item_price


some_stuff = Category('First category')

product1 = Product('First product', 140)
product2 = Product('Second product', 470)

some_stuff.add_product(product1)
some_stuff.add_product(product2)

print(some_stuff.get_count())
print(some_stuff.get_total_cost())

print(Category.total_with_sale(
    some_stuff.get_total_cost()
))
