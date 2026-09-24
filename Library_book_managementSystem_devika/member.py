class Member:
    def __init__(self,memid,name,ph_no):
        self.memid=memid
        self.name=name
        self.ph_no=ph_no

    def displaymembers(self):
        return self.memid+self.name+self.ph_no