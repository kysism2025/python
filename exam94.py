


class Book(object):
    def __init__(self, title, isbn):
        self._title = title
        self._isbn = isbn
    
    def __repr__(self): # __str__과 동일한 기능
        return "ISBN:" + self._isbn + ";TITLE:" + self._title
    
book = Book("The Python Tutorial", "0123456")    
print(book)