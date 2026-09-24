class LibraryMember:

    def __init__(self, memberID, name):
        self.memberID = memberID
        self.name = name

    def __repr__(self):
        return str(self.name)