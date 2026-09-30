# Global function
def promote_product(*args):
    print("promoting product on insta")


class ContentCreator:

    def create_content(self):
        print("creating product videos")


class Seller:

    def sell_product(self):
        print("selling product")


# Multiple inheritance
class InfluencerSeller(ContentCreator, Seller):

    def work(self):
        print("influencer is working")


person = InfluencerSeller()

# Methods from parent classes
person.create_content()
person.sell_product()

# Method from child class
person.work()

# Global function - call directly
promote_product()