from models.allergen import Allergen
import repositories.allergen_repository as allergen_repository

from models.cart_item import CartItem
import repositories.cart_item_repository as cart_item_repository

from models.product import Product
import repositories.product_repository as product_repository

from models.shopping_cart import ShoppingCart
import repositories.shopping_cart_repository as shopping_cart_repository

allergen_to_soy = Allergen('Milk', 'Many prdocts')
allergen_repository.save(allergen_to_soy)
print(allergen_to_soy.id)

allergen_repository.delete_by_id(5)

ex = allergen_repository.select_all()
for products in ex:
    print(products.id)


# res = allergen_repository.select(2)
# print(res.name)

product1 = Product('name', 'description', 2, 'image_url', 3, 5, allergen_to_soy)
product_repository.save(product1)
item1 = CartItem(1, product1)
cart_item_repository.save(item1)

shopping_cart_repository.save(item1)