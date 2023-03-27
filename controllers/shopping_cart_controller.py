from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
from models.cart_item import CartItem
from models.shopping_cart import ShoppingCart
import repositories.product_repository as product_repository
import repositories.allergen_repository as allergen_repository
import repositories.cart_item_repository as cart_item_repository
import repositories.shopping_cart_repository as shopping_cart_repository


product_blueprint = Blueprint("product", __name__)

# INDEX
@product_blueprint.route("/cart/add/<id>")
def add_product_to_cart(product_id: int):
    products = product_repository.select_all()
    allergens = allergen_repository.select_all()
    items_in_cart = cart_item_repository.quantity_of_products()


    product=product_repository.select(product_id)
    
    cart_item = CartItem(product_id=product_id, quantity=1)
    shopping_cart=ShoppingCart(items_in_cart)
    shopping_cart.add_cart_item(cart_item)




    return render_template("index.html", items_in_cart=items_in_cart, products=products, allergens=allergens)
