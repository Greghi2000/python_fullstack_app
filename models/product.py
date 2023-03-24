class Product:
    def __init__(self, name, description, price, image_url, rating, stock, allergen_id, id=None):
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url
        self.rating = rating
        self.stock = stock
        self.allergen_id = allergen_id
        self.id = id