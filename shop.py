class Product():
    def __init__(self, name, price, discount):
        self.name = name
        self._price = price
        self.discount = discount

    @property
    def price(self):
        if self._price < 0:
            raise Exception("цена меньше 0")
        return self._price 
    
    @property
    def total_price(self):
        if self._price < 0:
            raise Exception("цена меньше 0")
        if self.discount >  100:
            raise Exception("Скидка больше 100")
        return self.price - self.price*(self.discount/100)

    def __str__(self):
        return f"{self.name}: {self.price} руб. (скидка {self.discount}%)"
    

class DigitalProduct(Product):
    def __init__(self, name, price, discount, file_size):
        super().__init__(name, price, discount)
        self.file_size = file_size

    def download_info(self):
        return f"Скачать: {self.name} ({self.file_size} МБ)"


class PhysicalProduct(Product):
    def __init__(self, name, price, discount, weight):
        super().__init__(name, price, discount)
        self.weight = weight

    @property
    def shipping_cost(self):
        return self.weight * 1

    @property
    def total_price(self):
        return super().total_price + self.shipping_cost


class Cart():
    def __init__(self):
        self.basket = dict()

    def add(self, product: Product, count = 1):
        self.basket[product] = self.basket.get(product, 0) + count
        
    def remove(self, name: int = 1):
        for product in self.basket.keys:
            if product.name == name:
                if self.basket[product] == 0:
                    self.basket.pop(product)
                    return
                self.basket[product] -= 1
                return
        raise Exception("Товара нет в корзине")
    
    @property
    def total(self):
        cost = 0
        for product, count in self.basket.items():
            cost += product.total_price * count

        return cost



mouse = PhysicalProduct('mouse', 500, 10, 100)
print(mouse)
print(f"mouse total price: {mouse.total_price}")

game = DigitalProduct("Minecraft", 150, 0, 15555)
print(game, game.download_info())

cart = Cart()
cart.add(game, 2)
cart.add(mouse)
print(f"total price: {cart.total}")
