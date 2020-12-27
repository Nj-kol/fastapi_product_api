
from ..database import db
from ..models.product_models import Product
from ..schemas.product_schema import ProductBase


class ProductRepo:

    def add_product(self,new_product: ProductBase):
        db.session.add(new_product)
        db.session.commit()

    def get_all_products(self):
      all_products =  db.query(Product).all()
      return all_products

    def update_product(self,id,updated_product: ProductBase):
      product = Product.query.get(id)
      product.name = updated_product.name
      product.description = updated_product.description
      product.price = updated_product.price
      product.qty = updated_product.qty
      db.session.commit()
      return product

    def delete_product(self,id):
      product = Product.query.get(id)
      db.session.delete(product)
      db.session.commit()
