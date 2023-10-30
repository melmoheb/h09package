import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    #Initiate test case
    def setUp(self):
        self.test = BookLover('test', 'test@testmail.com', 'mystery')
        
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        self.test.add_book('Life of Pi', '4')
        # error message if fails
        message_1 = 'book not added as expected'
        # Expected output
        expected_1 = pd.DataFrame({'book_name': ['Life of Pi'],
                                   'book_rating': ['4']})
        # Assert test
        self.assertEqual(self.test.book_list.to_dict(orient='list'), expected_1.to_dict(orient='list'), message_1)
        
    def test_2_add_book(self):
        # Adding book that already exists
        self.test.add_book('Life of Pi', '4')
        self.test.add_book('Life of Pi', '4')
        # Expected output
        expected_2 = pd.DataFrame({'book_name': ['Life of Pi'], 'book_rating': ['4']})
        # Error message if test fails
        message_2 = 'Duplicate book was added to the book list'
        self.assertEqual(self.test.book_list.to_dict(orient='list'), expected_2.to_dict(orient='list'), message_2)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        self.test.add_book('Life of Pi', '4')
        # error message in case if test case got failed 
        message_3 = 'Test value is not True'
        # assert(True) to check if value is true
        self.assertTrue(self.test.has_read('Life of Pi'), message_3)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        self.test.add_book('Black Swan', '4')
        # error message in case if test case got failed 
        message4 = 'Test value is not False'
        # assert(True) to check if value is true
        self.assertFalse(self.test.has_read('Sapiens'), message4)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        self.test.add_book('Black Swan', '4')
        self.test.add_book('Life of Pi', '4')
        # Expected number of books read    
        expect_booknb = 2
        # Error message if test fails
        message5 = 'Number of books read did not match value expected'
        # Check if expect and actual outputs match
        self.assertEqual(expect_booknb, self.test.num_books_read(), message5)
        
    def test_6_fav_books(self):
        # Add book with poor rating
        self.test.add_book('The Good Son', '2')
        self.test.add_book('Life of Pi', '4')
        self.test.add_book('Black Swan', '4')
        # Actual dataframe
        testValue6 = self.test.fav_books()
        # Expected return
        expected_return = pd.DataFrame({'book_name': ['Life of Pi', 'Black Swan'],
                                       'book_rating': ['4', '4']})
        # Error message
        message6 = 'Returned dataframe did not match expected dataframe'
        # Your test should check that the returned books have rating  > 3
        self.assertEqual(expected_return.to_dict(orient='list'), testValue6.to_dict(orient='list'), message6)
        
if __name__ == '__main__':

    unittest.main(verbosity=3)
    
    
    
    