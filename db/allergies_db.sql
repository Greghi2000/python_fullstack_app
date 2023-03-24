DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS shopping_cart;
DROP TABLE IF EXISTS cart_item;
DROP TABLE IF EXISTS allergen;

CREATE TABLE allergen (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    product VARCHAR(255)
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255), 
    price INT, 
    image_url TEXT, 
    rating INT, 
    stock INT, 
    delivery_time VARCHAR(255),
    allergen_id INT REFERENCES allergen(id) 
);

CREATE TABLE cart_item (
    id SERIAL PRIMARY KEY,
    quantity INT,
    paroduct_id INT REFERENCES product(id)
);

CREATE TABLE shopping_cart (
    id SERIAL PRIMARY KEY,
    items_id INT REFERENCES cart_item(id)
);
