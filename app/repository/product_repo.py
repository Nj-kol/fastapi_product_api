from ..models.product_models import Product
from ..schemas.product_schema import ProductBase
from sqlalchemy.orm.session import Session


class ProductRepo:

    # parameterized constructor
    def __init__(self, db: Session):
        self.db = db

    def add_product(self, new_product: ProductBase):
        self.db.add(new_product)
        self.db.commit()

    def get_all_products(self):
        all_products = self.db.query(Product).all()
        # all_products =  self.db.query()
        return all_products

    def update_product(self, id, updated_product: ProductBase):
        product = Product.query.get(id)
        product.name = updated_product.name
        product.description = updated_product.description
        product.price = updated_product.price
        product.qty = updated_product.qty
        self.db.commit()
        return product

    def delete_product(self, id):
        product = Product.query.get(id)
        self.db.delete(product)
        self.db.commit()
