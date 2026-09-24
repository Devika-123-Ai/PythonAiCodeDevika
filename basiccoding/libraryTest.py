from libraryassignement import bookorganizer
from librarybook import LibraryBook
from librarymember import LibraryMember


class bookorganizerTest:

    library = bookorganizer()

    # b = LibraryBook("The Great Gatsby", "asd")
    # library.add_book(b)

    # print(library.list_books())

    m = LibraryMember("123", "Ram")

    b1 = LibraryBook("The Great Gatsby", "asd")

    library.lend_book(m, b1)

    print(library.all_BorrowedBooks())