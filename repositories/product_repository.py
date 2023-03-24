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