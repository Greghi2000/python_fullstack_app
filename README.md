Allergy Filter:

Build an app that allows a user to track what foods/products to eat given their allergies.

Overview:
The app should allow the admin to create and edit products, e.g. Gluten-Free bread, Nut-Free bars.
The app should allow the admin to create and edit allergens.
The app should display all the products a user has added to their cart.
The app should display all the products existing in the db.

Possible Extensions:

Have a total cost of all the items added to the cart.
Filter products by rating.

The app will follow CRUD principles and be able to do employ CRUD on most items.

<!-- 1. User(MIGHT) As extention
Attributes: user_id, username, email, password, shipping_address, billing_address
Methods: register(), login(), update_profile(), update_password(), add_address(), remove_address(), get_order_history() -->
2. Product
Attributes: product_id, name, description, price, image_url, allergens, rating, stock, delivery_time
Methods: get_product_details(), update_stock(), update_rating()
<!-- 3. Category (MIGHT)
Attributes: category_id, name, products (list of Product objects)
Methods: add_product(), remove_product(), get_products() -->
4. ShoppingCart
Attributes: cart_id, user (User object), items (list of CartItem objects)
Methods: add_item(), remove_item(), update_item_quantity(), get_total(), empty_cart()
5. CartItem
Attributes: product (Product object), quantity
Methods: update_quantity()
<!-- 6. Order(MOST LIKELY WONT)
Attributes: order_id, user (User object), items (list of OrderItem objects), order_date, shipping_address, billing_address, order_status
Methods: place_order(), cancel_order(), update_order_status(), get_order_details() -->
<!-- 7. OrderItem(MOST LIKELY WONT)
Attributes: product (Product object), quantity, price
Methods: None -->
<!-- 8. Review As extention
Attributes: review_id, user (User object), product (Product object), rating, comment, review_date
Methods: submit_review(), edit_review(), delete_review() -->
9. Allergen
Attributes: allergen_id, name, products (list of Product objects)
Methods: add_product(), remove_product(), get_products()