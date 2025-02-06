class Product:
    def __init__(self, product_id, name, price, discount=0.0, tax=0.0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.discount = discount
        self.tax = tax

    def calculate_price(self):
        """Calculate final price after tax and discount."""
        return self.price * (1 + self.tax) * (1 - self.discount)

    def __str__(self):
        return f"{self.product_id} - {self.name} - {self.price}"


class OfficialProduct(Product):
    def __init__(self, product_id, name, price):
        super().__init__(product_id, name, price, tax=0.1)


class NonOfficialProduct(Product):
    def __init__(self, product_id, name, price):
        super().__init__(product_id, name, price, discount=0.08, tax=0.0)
