from pydantic import BaseModel


# Pydantic models
class ProductBase(BaseModel):
   name: str
   description: str
   price: float
   qty: int
