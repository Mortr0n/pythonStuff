class Product:
    def __init__(self, price = 0, name="", category = "Sports"):
            self.name = name
            self.price = price
            self.category = category
    
    def update_price(self, percent_change, is_increased):
        percent_change = percent_change/100
        if(is_increased==True):
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        print(f"{self.name} in Category: {self.category} and priced at ${self.price}")
        return self
    
newShoes = Product(150, "Nike's", "Basketball shoes")

newShoes.print_info().update_price(35, True).print_info()

basketball = Product(25, "Basketball", "Sports")
baseball = Product(8, "Baseball", "Baseball stuff")