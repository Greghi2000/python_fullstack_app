from flask import Blueprint, Flask, redirect, render_template, request
import pdb
from models.product import Product
from models.allergen import Allergen
import repositories.product_repository as product_repository
import repositories.allergen_repository as allergen_repository
import repositories.cart_item_repository as cart_item_repository

allergen_blueprint = Blueprint("allergen", __name__)


# NEW ALLERGEN
@allergen_blueprint.route("/allergen/new")
def new_allergen():
    products = product_repository.select_all()
    allergens = allergen_repository.select_all()
    number_items_in_cart = cart_item_repository.quantity_of_products()
    return render_template("add-new-allergen.html", products=products, allergens=allergens, number_items_in_cart=number_items_in_cart)

# CREATE
@allergen_blueprint.route("/allergen/create", methods=["POST"])
def create_allergen_new():
    allergen_name = request.form["allergen-attribute"]
    allergen_description = request.form["allergen-description"]
    created_allergen = Allergen(allergen_name, allergen_description)
    allergen_repository.save(created_allergen)
    return redirect("/products")