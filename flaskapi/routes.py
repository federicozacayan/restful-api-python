from flask import request, jsonify
from flaskapi.models import Product
from flaskapi.schemas import ProductSchema, product_schema, products_schema
from flaskapi import app, db

# Get a Product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  product_schema = ProductSchema()
  return product_schema.jsonify(product), 200

# Save a Product
@app.route('/product', methods=['POST'])
def addProduct():
    name = request.json['name']
    admin = Product(name=name)
    db.session.add(admin)
    db.session.commit()
    return jsonify({'status':201}), 201


# Get All Products
@app.route('/product', methods=['GET'])
def getProducts():
    products = Product.query.all()
    n = db.session.query(Product.name).count()
    output = products_schema.dump(products);
    return jsonify({
        'q': n,
        'product' : output
    }), 200

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def deleteProduct(id):
    try:
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'status':'200'}), 200
    except:
        return jsonify({'status':'500'}), 500



# Update Product
@app.route('/product/<id>', methods=['PUT'])
def updateProduct(id):
  product = Product.query.get(id)
  name = request.json['name']
  product.name = name
  db.session.commit()

  return product_schema.jsonify(product), 200
