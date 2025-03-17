from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Set


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the product",
                       description="This is the price of add product")
    discount: int
    discounted_price: float
    tags: Set[str] = []


class User(BaseModel):
    name: str
    email: str


app = FastAPI()


@app.get("/user/admin")
async def get_admin():
    return {"This is admin page"}


@app.post("/purchase")
async def purchase(user: User, product: Product):
    return {"user": user, "product": product}


@app.post("/product/create/{product_id}")
async def create_product(product: Product, product_id: int, category: str):
    product.discounted_price = product.price - \
        (product.price * product.discount) / 100
    return {"product_id": product_id, "product": product, "category": category}


@app.post("/user/create")
async def create_user(profile: Profile):
    return profile
