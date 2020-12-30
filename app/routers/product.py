import logging

from ..database import db
from fastapi import APIRouter

from ..repository.product_repo import ProductRepo

router = APIRouter()

logger = logging.getLogger(__name__)

# Init repository
repo = ProductRepo(db)

# Get All Products
@router.get('/product')
async def get_products():
  logger.info('Got request for fetching all products')
  all_products = repo.get_all_products()
  return all_products
