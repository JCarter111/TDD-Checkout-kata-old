# import the Python unit test module
import unittest

def checkout(items):
    # checkout kata
    # 
    # possible solutions
    # count item in list and remove them to use loop
    # or count items going through the loop then apply a
    # discount when multiples of 2 or 3 (item mod 3) - preferred
    
    price  = 0

    #if items.count("b15") == 2:
    #    price = price + 45
    #elif items.count("a99") == 3:
        #price = price + 130
    #else:
        
    for item in items:

        if item == "a99":
            price = price + 50
        elif item == "b15":
            price = price + 30
        elif item == "c40":
            price = price + 60
        elif item == "t34":
            price = price + 99

    # there are special offers for a99 and b15
    # a99 - 3 items for 130
    # b15 - 2 items for 45
    # deduct from the price to implement these discounts
    # check if a99 has been purchased with any multiples of 3
    # need to deduct 20p from each set of 3 * a99
    if items.count("a99")//3 > 0:
        # deduct 20p from every 3 * a99 in the list of checkout items
        price = price - (items.count("a99")//3)*20
    
    #check if b15 has been purchased with any multiples of 2
    # need to deduct 15p from every set of 2 * b15
    if items.count("b15")//2 > 0:
        # deduct 15p from every 2 * b15 in the list of checkout items
        price = price - (items.count("b15")//2)*15

    return price

class CheckoutTests(unittest.TestCase):

    # test single a99
    def test_one_a99_costs_50(self):
        self.assertEqual(checkout(["a99"]),50)
    
    # test single b15
    def test_one_b15_costs_30(self):
        self.assertEqual(checkout(["b15"]),30) 
    
    # test single c40
    def test_one_c40_costs_60(self):
        self.assertEqual(checkout(["c40"]),60) 

    # test single t34
    def test_one_t34_costs_99(self):
        self.assertEqual(checkout(["t34"]),99) 

    # test a99, b15
    def test_one_a99_and_one_b15_costs_80(self):
        self.assertEqual(checkout(["a99","b15"]),80)

    # test c40 and t34
    def test_one_c40_and_one_t34_costs_159(self):
        self.assertEqual(checkout(["c40","t34"]),159)
    # test b15 and t34
    def test_one_b15_and_one_t34_costs_129(self):
        self.assertEqual(checkout(["b15","t34"]),129)

    # test one of each item in list
    def test_one_a99_one_t34_and_one_c40_and_one_b15_costs_189(self):
        self.assertEqual(checkout(["t34","c40","b15","a99"]),239)

    # test that discount is applied to 2 * b15 when no other items present
    def test_two_b15_costs_45(self):
        self.assertEqual(checkout(["b15","b15"]),45)

    # test that discount is applied to 3 * a99 when no other items present
    def test_three_a99_costs_130(self):
        self.assertEqual(checkout(["a99","a99","a99"]),130)

    # test that discount is applied to 2 * b15 when other items present
    def test_two_b15_and_c40_costs_105(self):
        self.assertEqual(checkout(["b15","c40","b15"]),105)

    # test that discount is applied to 3 * a99 when other items present
    def test_three_a99_and_c40_costs_190(self):
        self.assertEqual(checkout(["a99","c40","a99","a99"]),190)

    # test deduction applied to three items when 4 * a99 in the checkout items
    def test_four_a99(self):
        self.assertEqual(checkout(["a99","a99","a99","a99"]),180)

    # test deduction applied to two items when 3 * b15 in the checkout items
    def test_three_b15(self):
        self.assertEqual(checkout(["b15","b15","b15"]),75)

    # test deduction applied more than once e.g. 7 * a99, 11 * b15
    # items in random order
    def test_seven_a99_eleven_b15(self):
        self.assertEqual(
            checkout(["a99","b15","b15","b15","a99","b15","b15","a99","b15","a99","b15","b15","a99","a99","b15","b15","a99","b15"]),
            565)

    # test deduction applied more than one, with other items in the basket
    def test_nine_a99_seven_b15_two_c40_three_t34(self):
        self.assertEqual(
            checkout(["c40","a99","t34","b15","b15","a99","b15","c40","a99","b15","a99","b15","t34","t34","b15","a99","a99","b15","a99","a99","a99"]),
            972)

if __name__ == "__main__":
    unittest.main()