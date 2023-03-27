from flask import Blueprint, Flask, redirect, render_template, request
import pdb
from models.product import Product
import repositories.product_repository as product_repository
import repositories.allergen_repository as allergen_repository
import repositories.cart_item_repository as cart_item_repository

cart_item_blueprint = Blueprint("cart_item", __name__)

# ADD TO CART
@cart_item_blueprint.route("/cart-items")
def cart_items():
    items_in_cart = cart_item_repository.quantity_of_products()
    print(items_in_cart)
    return render_template("index.html", items_in_cart=items_in_cart)

#VIEW ALL
@cart_item_blueprint.route("/products/cart")
def total_cart_items():
    items_in_cart = cart_item_repository.quantity_of_products()
    total_items_in_cart = cart_item_repository.select_all()
    # product_list = []
    # pdb.set_trace()
    # for cart_item in total_items_in_cart:
    #     product_id = cart_item.product_id
    #     product = product_repository.select(product_id)
    #     product_list.append(product)
    #     cart_item = cart_item

    return render_template("cart-items.html", items_in_cart=items_in_cart, total_items_in_cart=total_items_in_cart)