from book import Book
from library import Library
from member import Member


class LibraryTest:
    library = Library()
    book = Book("101","Abc","xyz")
    library.create_book(book)

    book1 = Book("102","def","jn")
    library.create_book(book1)
    
    book2 = Book("103","ghi","dev")
    library.create_book(book2)
    
   
    member1 = Member("201","Ram","123")
    library.issue_book(member1,book)
    member = Member("202","dev","123567")
    library.issue_book(member,book)
    library.issue_book(member,book2)
    library.issue_book(member,book1)

    asd = library.list_books_borrowed_by_member(member)
    print(asd)

    booksSize = len(library.list_books())
    print("No of Books = ", booksSize)

    members = library.listofmembers()
    for m in members:
        print(m.displaymembers());

    # library.return_book(member,book);
    
    
    
    
