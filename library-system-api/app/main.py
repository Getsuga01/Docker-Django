from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

# Import das classes de schema (garante compatibilidade com os nomes)
from .schemas import BookCreate, BookRead, BookUpdate

app = FastAPI(title="Books API", description="API RESTful para gerenciar livros", version="1.0")

# Cria as tabelas no banco de dados, caso ainda não existam
models.Base.metadata.create_all(bind=database.engine)


# --- Dependência para obter sessão do banco ---
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- Rota inicial ---
@app.get("/")
def root():
    return {"message": "📚 API de Livros Online!"}


# --- CREATE ---
@app.post("/books/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# --- LIST ALL ---
@app.get("/books/", response_model=list[BookRead])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()


# --- RETRIEVE (Get by ID) ---
@app.get("/books/{book_id}", response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_book


# --- UPDATE ---
@app.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    for key, value in book.dict(exclude_unset=True).items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


# --- DELETE ---
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    db.delete(db_book)
    db.commit()
    return {"message": "Livro deletado com sucesso!"}
