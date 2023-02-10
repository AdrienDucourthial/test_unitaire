import unittest
from library import *

# Test class Book
class TestBook(unittest.TestCase):
  def test_init_worked(self):
    book_test = Book("Title", "Author")
    # Verifying the book has been correctly registered
    self.assertEqual(book_test.title, "Title")
    self.assertEqual(book_test.author, "Author")

  def test_check_out(self):
    book_test = Book("Title", "Author")
    book_test.check_out()
    self.assertEqual(book_test.is_checked_out, True)

  def test_check_in(self):
    book_test = Book("Title", "Author")
    book_test.check_in()
    self.assertEqual(book_test.is_checked_out, False)

# Test class Library
class TestLibrary(unittest.TestCase):
  def test_add_book(self):
    library = Library()
    book_a = Book("a", "a")
    self.assertEqual(len(library.books), 0)
    library.add_book(book_a)
    self.assertEqual(len(library.books), 1)
  
  def test_add_not_a_book(self):
    library = Library()
    with self.assertRaises(AttributeError):
      library.add_book("book_a")
  
  def test_check_out_book(self):
    library = Library()
    book_a = Book("a", "a")
    library.add_book(book_a)
    library.check_out_book(book_a.title)
    self.assertEqual(book_a, True)
  
  def test_check_in_book(self):
    library = Library()
    book_a = Book("a", "a")
    library.add_book(book_a)
    library.check_in_book(book_a.title)
    self.assertEqual(book_a, False)

# Test class Client
class TestClient(unittest.TestCase):
  def test_init_worked(self):
    client = Client("Name")
    self.assertEqual(client.name, "Name")
  
  def test_check_out_book(self):    
    client = Client("Name")
    library = Library()
    book = Book("Title", "Author")
    library.add_book(book)
    client.check_out_book(library, book.title)
    self.assertEqual(book.is_checked_out, True)
    self.assertEqual(len(client.checked_out_books), 1)
  
  def test_check_in_book(self):    
    client = Client("Name")
    library = Library()
    book = Book("Title", "Author")
    library.add_book(book)
    client.check_out_book(library, book.title)
    client.check_in_book(library, book.title)
    self.assertEqual(book.is_checked_out, False)
    self.assertEqual(len(client.checked_out_books), 0)


if __name__ == '__main__':
    unittest.main()