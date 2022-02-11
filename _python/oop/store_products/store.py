import product

class Store:
    def __init__(self, name="Default Store"):
        self.name = name
        self.product_list = []

    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self
    
    def sell_product(self, id):
        self.product_list.remove(self.product_list[id])
        return self
    
    def inflation(self, percent_increase):
        for product in self.product_list:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, percent_discount):
        for product in self.product_list:
            product.update_price(percent_discount, False)
        return self
    
    def print_products(self):
        for product in self.product_list:
            product.print_info()
        return self
    
bestbuy = Store("Best Buy")

bestbuy.add_product(product.newShoes).print_products().add_product(product.basketball).print_products().add_product(product.baseball).sell_product(1).print_products()
bestbuy.inflation(25).print_products().set_clearance(50).print_products()