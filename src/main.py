from fastapi import FastAPI, Body
from pydantic import BaseModel


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Product(BaseModel):
    name: str
    price: int
    discount: int
    discounted_price: float


app = FastAPI()


@app.get("/user/admin")
async def get_admin():
    return {"This is admin page"}


@app.post("/product/create")
async def create_product(product: Product, product_id: int, category: str):
    product.discounted_price = product.price - (product.price * product.discount) / 100
    return {'product_id': product_id, 'product': product, 'category': category}


@app.post("/user/create")
async def create_user(profile: Profile):
    return profile
