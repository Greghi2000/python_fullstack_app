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
    print("sc id: " + str(shopping_cart.items_id.id))
    values = [shopping_cart.items_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    shopping_cart.id = id

def select_all():
    shopping_carts = []
    sql = "SELECT * FROM shopping_cart"
    results = run_sql(sql)
    for row in results:
        cart_item = cart_item_repository.select(row["cart_item_id"])
        shopping_cart = ShoppingCart(cart_item, row['id'])
        shopping_carts.append(shopping_cart)
    return shopping_carts

def select(id):
    shopping_cart = None
    sql = "SELECT * FROM shopping_cart WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        cart_item = cart_item_repository.select(result["cart_item_id"])
        shopping_cart = ShoppingCart(cart_item, result['id'])
    return shopping_cart

def delete_all():
    sql = "DELETE FROM shopping_cart"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM shopping_cart WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(shopping_cart):
    sql = "UPDATE shopping_cart SET cart_item_id = %s WHERE id = %s"
    values = [shopping_cart.items_id, shopping_cart.id]
    run_sql(sql, values)