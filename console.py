import pdb
from models.allergen import Allergen
import repositories.allergen_repository as allergen_repository

from models.cart_item import CartItem
import repositories.cart_item_repository as cart_item_repository

from models.product import Product
import repositories.product_repository as product_repository

from models.shopping_cart import ShoppingCart
import repositories.shopping_cart_repository as shopping_cart_repository

shopping_cart_repository.delete_all()
cart_item_repository.delete_all()
product_repository.delete_all()
allergen_repository.delete_all()

allergen1 = Allergen('Soy', 'All products containing soy')
allergen_repository.save(allergen1)
allergen2 = Allergen('Flour', 'All products containing flour')
allergen_repository.save(allergen2)
# allergen_selected_1 = allergen_repository.select(18)
# print(allergen_selected_1) Select WORKS
all_allergies = allergen_repository.select_all()
for allergy in all_allergies:
    print(allergy.id)

allergen2.product = 'All products containing lactose'
allergen_repository.update(allergen2)

# allergen_repository.delete_by_id(35) If allergen is deleted all the product will delete as well. How to fix?
# APART FROM DELETE BUGGING OUT THE REST OF THE METHODS WORK.

product1 = Product('Soy Milk', 'This is soy milk', 2.99, 'image url', 4, 100,
              allergen1)
product_repository.save(product1)
product2 = Product('Pasta', 'This is pasta', 2.99, 'image url', 4, 100,
              allergen2)
product_repository.save(product2)
all_products = product_repository.select_all()
for product in all_products:
    print('start here')
    print(product.id)
    print(product.allergen_id.id)
    product_repository.select(product.id) # select WORKS
    # product_repository.delete(product.id) WORKS
    print('this!!!')
    products_without_allergens = (product_repository.select_all_without_allergens(product.allergen_id.id))
    for products_without_allergen in products_without_allergens:
        print(products_without_allergen.price)

print("Saving!")
product1 = Product('Soy Milk hello', 'This is soy milk', 2.99, 'image url', 4, 100,
              allergen2)
# product1.name = "bitch"
product_repository.update(product1) 
print("Saved!")

cart_item1 = CartItem(5, product1)
cart_item_repository.save(cart_item1)
cart_item2 = CartItem(15, product1)
cart_item_repository.save(cart_item2)
all_cart_items = cart_item_repository.select_all()
print(all_cart_items)
for cart in all_cart_items:
    print(cart.id)
    print(cart.product_id)
    print(product_repository.select(cart.product_id))
    test = product_repository.select(cart.product_id)
    print(test.name)
    # product_repository.delete(cart.product_id)

shopping_cart1 = ShoppingCart(cart_item1)

shopping_cart_repository.save(shopping_cart1)

print(cart_item_repository.quantity_of_products())


all_cart_prods = cart_item_repository.select_all()

for cart_item in all_cart_prods:
    products = cart_item.product_id
    print(cart_item.product_id)
    var = product_repository.select(products)
    print(var.description)

# UPDATE PRODUCT METHOD NOT WORKING CORRECTLY???