class Book:
    def __init__(self,id,title,author):
        self.id=id
        self.title=title
        self.author=author

    def display(self):
        return self.id + self.title + self.author

    def __repr__(self):
        return self.id +"  "+ self.title +"  "+ self.author
