from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
import repositories.product_repository as product_repository
import repositories.allergen_repository as allergen_repository

product_blueprint = Blueprint("product", __name__)

# INDEX
@product_blueprint.route("/index")
def products():
    products = product_repository.select_all()
    allergens = allergen_repository.select_all()
    # allergen_name = request.form['allergen-name'] # How to make the allergen filter work?? When i tick specific allergen how do i make only the prods that contain that allergen dissapear?
    return render_template("index.html", products=products, allergens=allergens)

# VIEW
@product_blueprint.route("/index/product/<id>")
def view_product(id):
    product = product_repository.select(id)
    return render_template("product.html", product=product)

# NEW
@product_blueprint.route("/product/new")
def new_product():
    products = product_repository.select_all()
    allergens = allergen_repository.select_all()
    return render_template("product-create.html", products=products, allergens=allergens)


# CREATE
@product_blueprint.route("/index", methods=["POST"])
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
    return redirect("/index")




# # CREATE
# @humans_blueprint.route("/humans", methods=["POST"])
# def create_human():
#     name = request.form["name"]
#     new_human = Human(name)
#     human_repository.save(new_human)
#     return redirect("/humans")


# # EDIT
# @humans_blueprint.route("/humans/<id>/edit")
# def edit_human(id):
#     human = human_repository.select(id)
#     return render_template('humans/edit.html', human=human)


# # UPDATE
# @humans_blueprint.route("/humans/<id>", methods=["POST"])
# def update_human(id):
#     name = request.form["name"]
#     human = Human(name, id)
#     human_repository.update(human)
#     return redirect("/humans")


# DELETE
@product_blueprint.route("/index/delete/<id>")
def delete_product(id):
    product_repository.delete(id)
    return redirect("/index")