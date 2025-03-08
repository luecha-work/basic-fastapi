from fastapi import FastAPI

app = FastAPI()

BOOK = [
    {'title': 'Title 1', 'author': 'Author 1', 'category': 'Category 1'},
    {'title': 'Title 2', 'author': 'Author 2', 'category': 'Category 2'},
    {'title': 'Title 3', 'author': 'Author 3', 'category': 'Category 3'},
    {'title': 'Title 4', 'author': 'Author 4', 'category': 'Category 4'},
    {'title': 'Title 5', 'author': 'Author 5', 'category': 'Category 5'},
    {'title': 'Title 6', 'author': 'Author 6', 'category': 'Category 6'},
    {'title': 'Title 7', 'author': 'Author 7', 'category': 'Category 7'},
    {'title': 'Title 8', 'author': 'Author 8', 'category': 'Category 8'},
    {'title': 'Title 9', 'author': 'Author 9', 'category': 'Category 9'},
    {'title': 'Title 10', 'author': 'Author 10', 'category': 'Category 10'}
]


@app.get("/books")
async def read_books():
    return BOOK

@app.get("/books/{bool_title}")
async def read_books(bool_title: str):
    for book in BOOK:
        if book.get('title').casefold() == bool_title.casefold():
            return book
    