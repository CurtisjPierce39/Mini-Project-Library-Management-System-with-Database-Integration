from connect_my_sql import connect_database
from mysql.connector import Error

class Book:

    def add_book(self, title, author_id, isbn, publication_date):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO Books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (title, author_id, isbn, publication_date))
                conn.commit()
                print("New Book Added Successfully!")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()

    def borrow_book(self, user_id, book_id, borrow_date, return_date):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO Borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, NULL)"
                cursor.execute(query, (user_id, book_id, borrow_date, return_date))
                cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
                conn.commit()
                print("Book Borrowed Added Successfully!")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()

    def return_book(self, book_id, borrowed_book):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE borrowed_books SET return_date = CURDATE() WHERE id = %s", (borrowed_book,))
                cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
                conn.commit()
                print("Book returned successfully!")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()

    def search_book(self, book_id):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT id, title, author_id, isbn, publication_date, availability FROM Books WHERE id = %s"
                cursor.execute(query, (book_id,))
                for row in cursor.fetchall():
                    print("ID ",row[0])
                    print("Title: ",row[1])
                    print("Author ID: ",row[2])
                    print("ISBN: ",row[3])
                    print("Publication Date: ",row[4])
                    print("Availability: ",row[5])
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()

    def display_all_books(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM Books"
                cursor.execute(query)
                for row in cursor.fetchall():
                    print("ID ",row[0])
                    print("Title: ",row[1])
                    print("Author ID: ",row[2])
                    print("ISBN: ",row[3])
                    print("Publication Date: ",row[4])
                    print("Availability: ",row[5])
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()
class User:

    def set__add_user(self, name, library_id):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
                cursor.execute(query, (name, library_id))
                conn.commit()
                print("New User Added Successfully!")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()

    def get__view_user(self, user_id):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT id, name, library_id FROM Users WHERE id = %s"
                cursor.execute(query, (user_id,))
                for row in cursor.fetchall():
                    print("ID ",row[0])
                    print("Name: ",row[1])
                    print("Library ID: ",row[2])
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()
                
    def get__display_users(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM Users"
                cursor.execute(query)
                for row in cursor.fetchall():
                    print("ID ",row[0])
                    print("Name: ",row[1])
                    print("Library ID: ",row[2])
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()
class Author:

    def add_author(self, name, biography):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
                cursor.execute(query, (name, biography))
                conn.commit()
                print("New Author Added Successfully!")
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()

    def view_author(self, author_id):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT id, name, biography FROM Authors WHERE id = %s"
                cursor.execute(query, (author_id,))
                for row in cursor.fetchall():
                    print("ID ",row[0])
                    print("Name: ",row[1])
                    print("Biography: ",row[2])
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()
                
    def display_authors(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM Authors"
                cursor.execute(query)
                for row in cursor.fetchall():
                    print("ID ",row[0])
                    print("Name: ",row[1])
                    print("Library ID: ",row[2])
            except Error as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                conn.close()
class UserInterface:
    
    def __init__(self):
        self.book = Book()
        self.user = User()
        self.author = Author()

    def main(self):
        while True:
            print("Welcome to the Library Management System")
            print("---Book---")
            print("1. Add a New Book")
            print("2. Borrow a Book")
            print("3. Return a Book")
            print("4. Search for a Book")
            print("5. Display all Books")
            print("---User Menu---")
            print("6. Add a New User")
            print("7. View User Details")
            print("8. Display all Users")
            print("---Author Menu---")
            print("9. Add a New Author")
            print("10. View Author Details")
            print("11. Display all Authors")
            print("12. Quit")

            choice = input("Please choose an option (1-12): ")

            if choice == '1':
                title = input("Please enter the book title: ")
                author_id = input("Please enter the author ID: ")
                isbn = input("Please enter ISBN: ")
                publication_date = input("Please enter publication date: ")
                self.book.add_book(title, author_id, isbn, publication_date)
            elif choice == '2':
                user_id = input("Please enter user ID: ")
                book_id = input("Please enter book ID: ")
                borrow_date = input("Please enter borrow date: ")
                return_date = input("Please enter return date: ")
                self.book.borrow_book(user_id, book_id, borrow_date, return_date)
            elif choice == '3':
                borrowed_book = input("Enter borrowed ID: ")
                book_id = input("Please enter book ID: ")
                self.book.return_book(book_id, borrowed_book)
            elif choice == '4':
                book_id = input("Please enter the book ID: ")
                self.book.search_book(book_id)
            elif choice == '5':
                self.book.display_all_books()

            elif choice == '6':
                name = input("Please enter user name: ")
                user_id = input("Please enter user ID: ")
                self.user.set__add_user(name, user_id)
            elif choice == '7':
                user_id = input("Please enter user id: ")
                self.user.get__view_user(user_id)
            elif choice == '8':
                self.user.get__display_users()

            elif choice == '9':
                name = input("Please enter the author's name: ")
                biography = input("Please enter biography: ")
                self.author.add_author(name, biography)
            elif choice == '10':
                author_id = input("Please enter author ID: ")
                self.author.view_author(author_id)
            elif choice == '11':
                self.author.display_authors()
            elif choice == '12':
                print("Exiting the Library Management System!!")
                print("Thank you! Come Again!!!")
                break
            else:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    use_book = Book()
    user_info = User()
    use_author = Author()
    user_interface = UserInterface()
    user_interface.main()