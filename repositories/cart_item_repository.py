from db.run_sql import run_sql
from models.allergen import Allergen
from models.cart_item import CartItem
from models.product import Product
from models.shopping_cart import ShoppingCart
import repositories.allergen_repository as allergen_repository
import repositories.product_repository as product_repository
import repositories.shopping_cart_repository as shopping_cart_repository

# def save(cart_item):
#     sql = "INSERT INTO cart_item (quantity, product_id) VALUES (%s, %s) RETURNING id"
#     values = [cart_item.quantity, cart_item.product_id.id]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     cart_item.id = id

def save(cart_item: CartItem):
    sql = "INSERT INTO cart_item (quantity, product_id) VALUES (%s, %s) RETURNING id"
    values = [cart_item.quantity, cart_item.product.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    cart_item.id = id
    return cart_item

def select_all():
    cart_items = []
    sql = "SELECT * FROM cart_item"
    results = run_sql(sql)
    for row in results:
        product=product_repository.select(row["product_id"])
        print("product", product)
        print("found product with id", product.id)
        cart_item = CartItem(quantity=row['quantity'], product=product, product_id=product.id,id=row['id'])
        cart_items.append(cart_item)
    return cart_items

def select(id):
    cart_item = None
    sql = "SELECT * FROM cart_item WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        product = product_repository.select(result["product_id"])
        cart_item = CartItem(result['quantity'], product, result['id'])
    return cart_item

def delete_all():
    sql = "DELETE FROM cart_item"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM cart_item WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(cart_item):
    sql = "UPDATE cart_item SET quantity = %s WHERE id = %s"
    values = [cart_item.quantity, cart_item.id]
    run_sql(sql, values)

def quantity_of_products() -> int:
    sql = "SELECT SUM (quantity) FROM cart_item"
    results = run_sql(sql)
    if results:
        result = results[0][0]
    return result