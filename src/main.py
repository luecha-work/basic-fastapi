from datetime import date, datetime, time, timedelta
from fastapi import FastAPI, Form
from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List
from uuid import UUID


class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: datetime
    end_time: datetime
    repeat_time: time
    execute_after: timedelta


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Image(BaseModel):
    url: HttpUrl
    name: str


class Product(BaseModel):
    name: str = Field(example="Phone")
    price: int = Field(title="Price of the product",
                       description="This is the price of add product")
    discount: int
    discounted_price: float
    tags: Set[str] = Field(example=["electronics", "phone"])
    image: List[Image] = []

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Phone",
                "price": 1000,
                "discount": 10,
                "discounted_price": 0,
                "tags": ["electronics", "phone"],
                "image": [
                    {
                        "url": "http://www.google.com",
                        "name": "phone image"
                    },
                    {
                        "url": "http://www.google.com",
                        "name": "phone image side view"
                    }
                ]
            }
        }


class Offer(BaseModel):
    name: str
    description: str
    price: float
    products: List[Product]


class User(BaseModel):
    name: str
    email: str


app = FastAPI()


@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


@app.post("/add-event")
def add_event(event: Event):
    return event


@app.get("/user/admin")
async def get_admin():
    return {"This is admin page"}


@app.post("/purchase")
async def purchase(user: User, product: Product):
    return {"user": user, "product": product}


@app.post("/add-offer")
async def add_offer(offer: Offer):
    return {offer: offer}


@app.post("/product/create/{product_id}")
async def create_product(product: Product, product_id: int, category: str):
    product.discounted_price = product.price - \
        (product.price * product.discount) / 100
    return {"product_id": product_id, "product": product, "category": category}


@app.post("/user/create")
async def create_user(profile: Profile):
    return profile
