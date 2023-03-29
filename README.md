Allergy Filter:

<!-- 1. User(MIGHT) As extention
Attributes: user_id, username, email, password, shipping_address, billing_address
Methods: register(), login(), update_profile(), update_password(), add_address(), remove_address(), get_order_history() -->
2. Product
Attributes: product_id, name, description, price, image_url, allergens, rating, stock
Methods: save(), update(), select_all(), select(), select_all_without_allergens(), delete_by_id(), delete()
<!-- 3. Category(MIGHT) As extention
Attributes: category_id, name, products (list of Product objects)
Methods: add_product(), remove_product(), get_products() -->
4. ShoppingCart
Attributes: cart_id, user (User object), items (list of CartItem objects)
Methods: save(), update(), select_all(), select(), delete_by_id(), delete()
5. CartItem
Attributes: product (Product object), quantity
Methods: save(), update(), select_all(), select(), delete_by_id(), delete(), quantity_of_products()
9. Allergen
Attributes: allergen_id, name, products (list of Product objects)
Methods: save(), update(), select_all(), select(), delete_by_id(), delete()