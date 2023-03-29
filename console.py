import pdb
from models.allergen import Allergen
import repositories.allergen_repository as allergen_repository

from models.cart_item import CartItem
import repositories.cart_item_repository as cart_item_repository

from models.product import Product
import repositories.product_repository as product_repository

from models.shopping_cart import ShoppingCart
import repositories.shopping_cart_repository as shopping_cart_repository

shopping_cart_repository.delete_all()
cart_item_repository.delete_all()
product_repository.delete_all()
allergen_repository.delete_all()

# ALLERGENS
allergen1 = Allergen('Soy', 'All products containing soy')
allergen_repository.save(allergen1)
allergen2 = Allergen('Flour', 'All products containing flour')
allergen_repository.save(allergen2)

#PRODUCTS
product1 = Product('Soy Sauce', 'A classic sauce made from fermented soybeans', 
                   3.99, 'https://images.immediate.co.uk/production/volatile/sites/30/2020/02/Soy-sauce-2e1d5da.jpg?resize=960,872', 4.2, 50, allergen1)

product2 = Product('Flour Tortillas', 'Soft and chewy tortillas perfect for wrapping up your favorite fillings', 
                   2.49, 'https://upload.wikimedia.org/wikipedia/commons/5/56/NCI_flour_tortillas.jpg', 4.5, 75, allergen2)

product3 = Product('Soy Milk', 'A dairy-free milk alternative made from soybeans', 
                   4.99, 'https://post.healthline.com/wp-content/uploads/2022/05/soy-milk-bottle-732-549-feature-thumb.jpg', 4.1, 60, allergen1)

product4 = Product('Chocolate Cake', 'A rich and decadent chocolate cake made without flour', 
                   19.99, 'https://sugarfreelondoner.com/wp-content/uploads/2020/12/sugar-free-birthday-cake-chocolate-1200.jpg', 4.8, 20, allergen2)

product5 = Product('Soy Nuts', 'A crunchy and healthy snack made from roasted soybeans', 
                   1.99, "https://cdn.shopify.com/s/files/1/0075/9549/1441/products/467-4_800x.jpg?v=1666852651", 4.3, 100, allergen1)

product6 = Product('Gluten-Free Flour Blend', 'A versatile flour blend that can be used in place of wheat flour in many recipes', 
                   6.99, 'https://littlespoonfarm.com/wp-content/uploads/2021/09/Gluten-free-flour-blend-recipe-500x375.jpg', 4.6, 30, allergen2)
product7 = Product('Soy Burger', 'A plant-based burger patty made from soy protein', 
                   5.99, 'https://www.stayathomemum.com.au/wp-content/uploads/2011/10/Soy-Bean-Burger-Patties-.jpg', 4.4, 40, allergen1)

product8 = Product('All-Purpose Flour', 'A pantry staple for baking and cooking', 
                   2.29, 'https://www.spatuladesserts.com/wp-content/uploads/2022/07/is-all-purpose-flour-the-same-as-plain-flour_3.jpg', 4.7, 90, allergen2)

product9 = Product('Edamame', 'A healthy and protein-packed snack made from immature soybeans', 
                   3.49, 'https://evergreenkitchen.ca/wp-content/uploads/2021/10/Sesame-Spiced-Edamame-0-4X5-500x500.jpg', 4.2, 80, allergen1)

product10 = Product('Soy Yogurt', 'A dairy-free yogurt alternative made from soy milk', 
                    1.99, 'https://yumveganlunchideas.com/wp-content/uploads/2020/08/soy-greek-yogurt-scaled.jpg', 4.0, 70, allergen1)

product11 = Product('Almond Flour Bread', 'A gluten-free bread made with almond flour instead of wheat flour', 
                    6.99, 'https://foolproofliving.com/wp-content/uploads/2020/01/Almond-Flour-Bread-Recipe-Image.jpg', 4.5, 25, allergen2)

product12 = Product('Soy Sauce Powder', 'A convenient and versatile powder form of soy sauce', 
                    4.99, 'https://www.tastesensationltd.com/wp-content/uploads/2022/04/AMAZON-SOY-SAUCE-POWDER-IMAGE-1-2-scaled.jpg', 4.1, 50, allergen1)
product_repository.save(product1)
product_repository.save(product2)
product_repository.save(product3)
product_repository.save(product4)
product_repository.save(product5)
product_repository.save(product6)
product_repository.save(product7)
product_repository.save(product8)
product_repository.save(product9)
product_repository.save(product10)
product_repository.save(product11)
product_repository.save(product12)

#ITEMS IN CART
cart_item1 = CartItem(5, product1, product1.id)
cart_item1 = cart_item_repository.save(cart_item1)
cart_item2 = CartItem(1, product2, product2.id)
cart_item2 = cart_item_repository.save(cart_item2)
print(cart_item1.id)
cart_item_repository.delete_by_id(cart_item1.id)