from flask_marshmallow import Marshmallow
from flaskapi.models import Product
from flaskapi import app, db

ma = Marshmallow(app)
class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

#create database after define schemas
db.create_all()
