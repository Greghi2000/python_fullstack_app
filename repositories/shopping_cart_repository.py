from db.run_sql import run_sql
from models.allergen import Allergen
from models.cart_item import CartItem
from models.product import Product
from models.shopping_cart import ShoppingCart
import repositories.allergen_repository as allergen_repository
import repositories.cart_item_repository as cart_item_repository
import repositories.product_repository as product_repository

def save(shopping_cart):
    sql = "INSERT INTO shopping_cart (cart_item_id) VALUES (%s) RETURNING id"
    values = [shopping_cart.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    shopping_cart.id = id