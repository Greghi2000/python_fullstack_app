from models.cart_item import CartItem


class ShoppingCart:
    def __init__(self, items: list[CartItem], id=None):
        self.items = items
        self.id = id

    def addItem(self, item: CartItem):
        self.items.append(item)

    def getItems(self):
        return self.items
    
    def getItemById(self, id):
        for i in self.items:
            if i.product_id==id:
                return i
        return None
