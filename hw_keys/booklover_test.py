import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.

        book_lover = BookLover("RCA", "a@b.com", "scifi")
        test_name = "Test Book"
        test_rating = 5
        book_lover.add_book(test_name, test_rating)
        self.assertTrue(book_lover.has_read(test_name))

    def test_2_add_book(self):
        # add the same book twice. Test it's in `book_list` only once.
        
        book_lover = BookLover("RCA", "a@b.com",  "scifi")
        test_name = "Test Book"
        test_rating = 5
        book_lover.add_book(test_name, test_rating)
        book_lover.add_book(test_name, test_rating)
        expected = 1
        actual = len(book_lover.book_list[book_lover.book_list.book_name == test_name])
        self.assertEqual(expected, actual)
        
    def test_3_has_read(self): 
        # pass a book in the list and test the answer is `True`.
        
        book_lover = BookLover("RCA", "a@b.com",  "scifi")
        test_name = "Test Book"
        test_rating = 5
        book_lover.add_book(test_name, test_rating)
        self.assertTrue(book_lover.has_read(test_name))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test if the answer is `True`
        
        book_lover = BookLover("RCA", "a@b.com",  "scifi")
        test_name = "Test Book"
        self.assertFalse(book_lover.has_read(test_name))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        
        book_lover = BookLover("RCA", "a@b.com",  "scifi")
        test_books = [
            ("Jane Eyre", 4), 
            ("Fight Club", 3),
            ("The Divine Comedy", 5),
            ("The Popol Vuh", 5) 
        ]
        for book in test_books:
            book_lover.add_book(*book)
        
        self.assertEqual(len(test_books), book_lover.num_books_read())

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating $> 3$. 
        # Your test should check that the returned books have rating $ > 3
        
        book_lover = BookLover("RCA", "a@b.com",  "scifi")
        test_books = [
            ("Jane Eyre", 4), 
            ("Fight Club", 3),
            ("The Divine Comedy", 5),
            ("The Popol Vuh", 5) 
        ]
        for book in test_books:
            book_lover.add_book(*book)

        actual = len(book_lover.fav_books())
        expected = len([x for x, y in test_books if y > 3])
        self.assertEqual(actual, expected)
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)