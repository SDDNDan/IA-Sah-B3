import unittest
from Product import Product

class Product_Test(unittest.TestCase):
    
    # Arrange for all tests
    product = Product("Rolex watch", 100, 4, "A very classy watch from Rolex")

    def test_WhenProductExists_WeChangeName_ShouldUpdateName(self):
        # ACT
        newName = self.product.changeName("Another Rolex watch")

        # ASSERT
        self.assertEqual(newName, "Another Rolex watch", "Error in changeName function!")

    def test_WhenProductExists_WeChangeRatingWithInvalidParam_ShouldNotUpdateRating(self):
        #ACT
        newRating = self.product.changeRating(6)

        # ASSERT
        self.assertNotEqual(newRating, 6, "Error in changeRating function!")

    def test_WhenProductExists_WeCallApplyDiscountMethod_ShouldUpdatePrice(self):
        #ACT
        newPrice = self.product.applyDiscount(25)

        # ASSERT
        self.assertEqual(newPrice, 75, "Error in applyDiscount function!")

if __name__ == '__main__':
    unittest.main()