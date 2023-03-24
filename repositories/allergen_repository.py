import pdb
from db.run_sql import run_sql
from models.allergen import Allergen
from models.cart_item import CartItem
from models.product import Product
from models.shopping_cart import ShoppingCart
import repositories.cart_item_repository as cart_item_repository
import repositories.product_repository as product_repository
import repositories.shopping_cart_repository as shopping_cart_repository

def save(allergen):
    sql = "INSERT INTO allergen (name, product) VALUES (%s, %s) RETURNING id"
    values = [allergen.name, allergen.product]
    results = run_sql(sql, values)
    id = results[0]['id']
    allergen.id = id
    # pdb.set_trace()

def select_all():
    allergens = []
    sql = "SELECT * FROM allergen"
    results = run_sql(sql)
    for row in results:
        allergen = Allergen(row['name'], row['product'], row['id'])
        allergens.append(allergen)
    return allergens

def select(id):
    allergen = None
    sql = "SELECT * FROM allergen WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        allergen = Allergen(result['name'], result['product'], result['id'])
    return allergen

def delete_all():
    sql = "DELETE FROM allergen"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM allergen WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(allergen):
    sql = "UPDATE allergen SET name = %s WHERE id = %s"
    values = [allergen.name, allergen.id]
    run_sql(sql, values)
