class Product:
    def __init__(self, name, price, rating, description):
        self.name = name
        self.price = price
        self.rating = rating
        self.description = description

    def changeName(self, newName):
        self.name = newName
        return self.name

    def changePrice(self, newPrice):
        self.price = newPrice
        return self.price

    def changeRating(self, newRating):
        if newRating <= 5 and newRating >= 0:
            self.rating = newRating
        return self.rating

    def changeDescription(self, newDescription):
        self.description = newDescription
        return self.description

    def applyDiscount(self, procentage):
        self.price = self.price - (self.price / 100) * procentage
        return self.price
    

    