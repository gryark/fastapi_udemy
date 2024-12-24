from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "genre": "Fantasy"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954, "genre": "Fantasy"},
    {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "year": 1943, "genre": "Children's literature"},
    {"title": "And Then There Were None", "author": "Agatha Christie", "year": 1939, "genre": "Mystery"},
    {"title": "Dream of the Red Chamber", "author": "Cao Xueqin", "year": 1791, "genre": "Family saga"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy"},
    {"title": "She: A History of Adventure", "author": "H. Rider Haggard", "year": 1887, "genre": "Adventure"},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003, "genre": "Mystery"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "genre": "Realistic fiction"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "genre": "Fantasy"}
 
]

@app.get("/books")
def get_all_books():
    return BOOKS