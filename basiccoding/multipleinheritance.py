company = "Amazon"       # Global variable


class ContentCreator:

    def create_content(self):
        print("Creating content for", company)


class Seller:

    def sell_product(self):
        print("Selling product for", company)


class InfluencerSeller(ContentCreator, Seller):

    def promote_product(self):
        print("Promoting product for", company)


person = InfluencerSeller()

person.create_content()
person.sell_product()
person.promote_product()
print(company)