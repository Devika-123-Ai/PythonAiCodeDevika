class bookorganizer:
    member_books = {};
    books = [];

    def __init__(self):
        self.books = []
        self.member_books ={}

    def add_book(self, book):        
        self.books.append(book)

    def list_books(self):
        return self.books  
    
    def lend_book(self,membership,book):
        self.member_books[membership] = book

    def all_BorrowedBooks(self):
        return self.member_books
    
