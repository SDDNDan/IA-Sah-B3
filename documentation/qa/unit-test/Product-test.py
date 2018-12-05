import unittest
from Product import Product

class Product_Test(unittest.TestCase):
    
    def setUp(self):
        self.producd = Product("Rolex watch", 100, 4, "A very classy watch from Rolex")

    def testChangeName(self):
        newName = self.product.changeName("Another Rolex watch")

        self.assertEqual(newName, "Another Rolex watch", "Error in changeName function!")

    def testChangeRating(self):
        newRating = self.product.changeRating(6)

        self.assertNotEqual(newRating, 6, "Error in changeRating function!")

    def testApplyDiscount(self):
        newPrice = self.product.applyDiscount(25)

        self.assertEqual(newPrice, 75, "Error in applyDiscount function!")

if __name__ == '__main__':
    unittest.main()