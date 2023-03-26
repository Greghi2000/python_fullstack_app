from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
import repositories.product_repository as product_repository
import repositories.allergen_repository as allergen_repository
import repositories.cart_item_repository as cart_item_repository

product_blueprint = Blueprint("product", __name__)

# ADD TO CART
@product_blueprint.route("/index")
def products():
    items_in_cart = cart_item_repository.quantity_of_products()
    return render_template("index.html", items_in_cart=items_in_cart)