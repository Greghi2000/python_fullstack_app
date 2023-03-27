from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
from models.cart_item import CartItem
from models.shopping_cart import ShoppingCart
import repositories.product_repository as product_repository
import repositories.allergen_repository as allergen_repository
import repositories.cart_item_repository as cart_item_repository
import repositories.shopping_cart_repository as shopping_cart_repository


shopping_cart_blueprint = Blueprint("shopping_cart", __name__)

# INDEX
@shopping_cart_blueprint.route("/cart/add/<id>")
def add_product_to_cart(id: int):
    print("id of the product to add", id)
    products = product_repository.select_all()
    allergens = allergen_repository.select_all()
    items_in_cart = cart_item_repository.select_all()
    number_items_in_cart=0
    for item in items_in_cart:
        number_items_in_cart = number_items_in_cart + item.quantity

    product=product_repository.select(id)
    print("product in add to cart", product)

    cart_item = CartItem(product=product, quantity=1, product_id=product.id)
    cart_item = cart_item_repository.save(cart_item)
    shopping_cart=ShoppingCart(items_in_cart)
    shopping_cart.addItem(cart_item)
    shopping_cart_repository.save(shopping_cart)
    return redirect("/products")
    # return render_template("index.html", number_items_in_cart=number_items_in_cart, items_in_cart=items_in_cart, products=products, allergens=allergens)
