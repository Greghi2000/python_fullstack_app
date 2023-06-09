from flask import Blueprint, Flask, redirect, render_template, request
import pdb
from models.product import Product
import repositories.product_repository as product_repository
import repositories.allergen_repository as allergen_repository
import repositories.cart_item_repository as cart_item_repository


product_blueprint = Blueprint("product", __name__)

# INDEX
@product_blueprint.route("/products")
def products():
    # pdb.set_trace()
    products = product_repository.select_all()
    allergens = allergen_repository.select_all()
    # items_in_cart = cart_item_repository.quantity_of_products()
    items_in_cart=cart_item_repository.select_all()
    number_items_in_cart=0
    for item in items_in_cart:
        number_items_in_cart = number_items_in_cart + item.quantity
    return render_template("index.html", number_items_in_cart=number_items_in_cart, items_in_cart=items_in_cart, products=products, allergens=allergens)

#FILTER FOR ALLERGENS
@product_blueprint.route("/products/filter/<allergen_id>")
def filter_products_by_allergen(allergen_id):
    products = product_repository.select_all_without_allergens(allergen_id)
    allergens = allergen_repository.select_all()
    items_in_cart = cart_item_repository.quantity_of_products()
    return render_template("index.html", number_items_in_cart=items_in_cart, products=products, allergens=allergens)

# VIEW
@product_blueprint.route("/products/<id>")
def view_product(id):
    product = product_repository.select(id)
    items_in_cart = cart_item_repository.quantity_of_products()
    return render_template("product.html", product=product, items_in_cart=items_in_cart)

# NEW
@product_blueprint.route("/products/new")
def new_product():
    products = product_repository.select_all()
    allergens = allergen_repository.select_all()
    return render_template("add-new-product.html", products=products, allergens=allergens)

# EDIT
@product_blueprint.route("/products/edit/<id>")
def edit_product(id):
    product = product_repository.select(id)
    allergens = allergen_repository.select_all()
    items_in_cart = cart_item_repository.quantity_of_products()
    return render_template("edit-product.html", items_in_cart=items_in_cart, product=product, allergens=allergens)

# EDIT POST
@product_blueprint.route("/products/edit/<id>", methods=["POST"])
def edit_product_post(id):
    id = id
    product = request.form["product"]
    description = request.form["description"]
    price = request.form["price"]
    image_url = request.form["img-url"]
    rating = request.form["rating"]
    stock = request.form["stock"]
    allergen_id = request.form["allergen_id"]
    allergen = allergen_repository.select(allergen_id)
    edited_product = Product(product, description, price, image_url, rating, stock, allergen, id)
    product_repository.update(edited_product)
    return redirect("/products")


# CREATE
@product_blueprint.route("/products/create", methods=["POST"])
def create_product_new():
    product = request.form["product"]
    description = request.form["description"]
    price = request.form["price"]
    image_url = request.form["img-url"]
    rating = request.form["rating"]
    stock = request.form["stock"]
    allergen_id = request.form["allergen_id"]
    allergen = allergen_repository.select(allergen_id)
    created_product = Product(product, description, price, image_url, rating, stock, allergen)
    product_repository.save(created_product)
    return redirect("/products")


# # UPDATE
# @humans_blueprint.route("/humans/<id>", methods=["POST"])
# def update_human(id):
#     name = request.form["name"]
#     human = Human(name, id)
#     human_repository.update(human)
#     return redirect("/humans")


# DELETE
@product_blueprint.route("/products/delete/<id>")
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")


# # UPDATE
# @product_blueprint.route("/products/update/<id>")
# def edit_product(id):
#     product_repository.update(id, )
#     return redirect("/products")