from models.cart_item import CartItem


class ShoppingCart:
    def __init__(self, items: list[CartItem], id=None):
        self.items = items
        self.id = id

    def add_item(self, item: CartItem):
        self.items.append(item)

    def remove_item(self, item: CartItem):
        id = item.id
        for i in self.items:
            if i.id == id:
                self.items.remove(i)

    def get_items(self):
        return self.items
    
    
    def get_item_by_id(self, id):
        for i in self.items:
            if i.product_id==id:
                return i
        return None
