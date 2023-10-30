import pandas as pd

class BookLover:
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, book_rating):
        new_book = pd.DataFrame({
        'book_name': [book_name], 
        'book_rating': [book_rating]})
        if new_book.book_name.values not in self.book_list.book_name.values:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            return f"'{book_name}' was added to the book list!"
        else:
            return f"'{book_name}' already exists!"
    
    def num_books_read(self):
        self.num_books = len(self.book_list)
        return self.num_books
    
    def has_read(self, book_name):
        return book_name in self.book_list.book_name.values
    
    def fav_books(self):
         return self.book_list[self.book_list.book_rating.astype(float) >3]
        
if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    
    # Add book and print the result
    result = test_object.add_book("War of the Worlds", 4)
    print(result)
    
    # Print the number of books read
    num_books = test_object.num_books_read()
    print(f"Number of books read: {num_books}")
    
    # Check if a book has been read and print the result
    book_name = "War of the Worlds"
    has_read = test_object.has_read(book_name)
    print(f"Has read '{book_name}': {has_read}")
    
    # Print favorite books
    fav_books = test_object.fav_books()
    print("Favorite books:")
    print(fav_books)