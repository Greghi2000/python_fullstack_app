from flask import Flask, render_template

from controllers.allergen_controller import allergen_blueprint
from controllers.cart_item_controller import cart_item_blueprint
from controllers.product_controller import product_blueprint
from controllers.shopping_cart_controller import shopping_cart_blueprint

app = Flask(__name__)
app.register_blueprint(allergen_blueprint)
app.register_blueprint(cart_item_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(shopping_cart_blueprint)

@app.route("/")
def main():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
