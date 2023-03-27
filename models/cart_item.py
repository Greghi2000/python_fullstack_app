from models.product import Product


class CartItem:
    def __init__(self, quantity: int, product: Product, product_id, id=None):
        self.quantity = quantity
        self.product_id = product_id
        self.id = id
        self.product=product
