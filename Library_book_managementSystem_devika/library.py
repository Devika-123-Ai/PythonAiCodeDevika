class Library:
    def __init__(self):
        self.book_list=[]
        self.memberbooks={}

    def create_book(self,book):
        self.book_list.append(book)

    def issue_book(self,member,book):
        if member not in self.memberbooks :
             self.memberbooks[member] =[]
        self.memberbooks[member].append(book)

    def return_book(self,member,book):
        if member in self.memberbooks :
            self.memberbooks[member].remove(book)

    def list_books(self):
        return self.book_list

    #  def list_books_borrowed_by_member(self,member):
    # // search memberbooks for member 

    def list_books_borrowed_by_member(self,member):
        for a in self.memberbooks:
            if(a.memid==member.memid):
                return self.memberbooks[a]
    def listofmembers(self):
        keys = list(self.memberbooks.keys())
        return keys
    
            
#  def book_details(self,bookId):
#  # //seach for the id in list of books
            
    def book_details(self,bookId):
        for a in self.book_list:
            if(a.bookId==bookId):
                return a

   