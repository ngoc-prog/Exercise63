class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        existing_product = self.get_product_by_id(product.product_id)
        if existing_product:
            self.remove_product(product.product_id)
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def search_by_name(self, keyword):
        return [p for p in self.products if keyword.lower() in p.name.lower()]

    def filter_by_price(self, min_price, max_price):
        return [p for p in self.products if min_price <= p.calculate_price() <= max_price]

    def get_all_products(self):
        return self.products
