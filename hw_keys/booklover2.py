import pandas as pd

class BookLover():

    """
    This version uses a dataframe with an index.
    """

    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_rating':[]}, index=[])

    def add_book(self, book_name, book_rating):
        if not self.has_read(book_name):
            self.book_list.loc[book_name, 'book_rating'] = book_rating
            
    def has_read(self, book_name):
        try:
            self.book_list.loc[book_name]
            return True
        except KeyError:
            return False
    
    def num_books_read(self):
        return(len(self.book_list))
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]