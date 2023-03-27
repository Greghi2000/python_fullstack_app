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
    items_in_cart = cart_item_repository.quantity_of_products()
    return render_template("index.html", items_in_cart=items_in_cart, products=products, allergens=allergens)

@product_blueprint.route("/products/filter/<allergen_id>")
def filter_products_by_allergen(allergen_id):
    products = product_repository.select_all_without_allergens(allergen_id)
    allergens = allergen_repository.select_all()
    # allergen_name = request.form['allergen-name'] # How to make the allergen filter work?? When i tick specific allergen how do i make only the prods that contain that allergen dissapear?
    items_in_cart = cart_item_repository.quantity_of_products()
    return render_template("index.html", items_in_cart=items_in_cart, products=products, allergens=allergens)

# VIEW
@product_blueprint.route("/products/<id>")
def view_product(id):
    product = product_repository.select(id)
    return render_template("product.html", product=product)

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
    return render_template("edit-product.html", product=product, allergens=allergens)

# EDIT POST
@product_blueprint.route("/products/edit", methods=["POST"])
def edit_product_post():
    product = request.form["product"]
    description = request.form["description"]
    price = request.form["price"]
    image_url = request.form["img-url"]
    rating = request.form["rating"]
    stock = request.form["stock"]
    allergen_id = request.form["allergen_id"]
    allergen = allergen_repository.select(allergen_id)
    edited_product = Product(product, description, price, image_url, rating, stock, allergen)
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