from classses import Author, BookItem, BookStore
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

myBookItemsDict:Dict[str, BookItem] = {}

@app.put("/books/{name}")
def createBook(book:BookItem,name:str) -> None:
    myBookItemsDict[name] = book
    print(myBookItemsDict.keys())

@app.get("/books/{name}")
def readBook(name: str) -> BookItem:
    if name in myBookItemsDict.keys():
        return {"Book": myBookItemsDict[name]}
    else:
        raise HTTPException(status_code=404, details= "no book found")
    
@app.delete("/books/{name}")
def deleteBook(name: str) -> Dict:
    if name in myBookItemsDict.keys():
        return {"message": "Item has been deleted"}
    else:
        raise HTTPException(status_code=404, details= "no book found")
    
@app.get("/books/")
def getBooks() -> List[BookItem]:
    return myBookItemsDict.values()