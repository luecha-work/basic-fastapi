from fastapi import FastAPI, Body
from pydantic import BaseModel


class Profile(BaseModel):
    name: str
    email: str
    age: int


app = FastAPI()


@app.get("/user/admin")
async def get_admin():
    return {"This is admin page"}


@app.post("/user/create")
async def create_user(profile: Profile):
    return profile
