from db.run_sql import run_sql
from models.allergen import Allergen
from models.cart_item import CartItem
from models.product import Product
from models.shopping_cart import ShoppingCart
import repositories.allergen_repository as allergen_repository
import repositories.cart_item_repository as cart_item_repository
import repositories.shopping_cart_repository as shopping_cart_repository

def save(product):
    sql = "INSERT INTO product (name, description, price, image_url, rating, stock, allergen_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.description, product.price, product.image_url, product.rating, product.stock,
              product.allergen_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id

def select_all():
    products = []
    sql = "SELECT * FROM product"
    results = run_sql(sql)
    for row in results:
        allergen = allergen_repository.select(row["allergen_id"])
        product = Product(row['name'], row['description'], row['price'], row['image_url'], 
                          row['rating'], row['stock'], allergen, row['id'])
        products.append(product)
    return products

def select_all_without_allergens(allergen):
    products = []
    sql = """SELECT *
        FROM product
        WHERE allergen_id <> %s"""
    values = [allergen]
    results = run_sql(sql, values)
    for row in results:
        allergen = allergen_repository.select(row["allergen_id"])
        product = Product(row['name'], row['description'], row['price'], row['image_url'], 
                          row['rating'], row['stock'], allergen, row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM product WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        allergen = allergen_repository.select(result["allergen_id"])
        product = Product(result['name'], result['description'], result['price'], result['image_url'], 
                          result['rating'], result['stock'], allergen.id, result['id'])
    return product

def delete_all():
    sql = "DELETE FROM product"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM product WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(product):
    sql = """UPDATE product SET (name, description, price, image_url, rating, stock, allergen_id) 
    = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"""
    values = [product.name, product.description, product.price, product.image_url, product.rating, product.stock,
              product.allergen_id.id, product.id]
    run_sql(sql, values)