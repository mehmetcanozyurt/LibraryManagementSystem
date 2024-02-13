# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:37:19 2024

@author: Mehmet Can
"""
class Library():
    
    def __init__(self,filename = "books.txt"):
        """
        Open the book file in read/append mode.
        """
        self.filename = filename
        try:
            with open(self.filename, "a+") as file:
                pass
        except:
            print("File not found.")
    
    def __del__(self):
        """
        Close the book file.
        """
        self.close.file()
        
    def list_books(self):
        """
        Shows book list
        """
        try:
            with open(self.filename, "r") as file:
                books = file.readlines()
            for book in books:
                title, author, *_ = book.strip().split(",")
                print(f"Book: {title}, Author: {author}")
        except FileNotFoundError:
            print("No books found in the library.")
            
    def add_book(self):
        """ 
        Add to book file
        """
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        
        book_info = f"{title},{author},{release_year},{num_pages}"
        try:
            with open(self.filename, "a") as file:
                file.write(book_info + "\n")
            print("Book added successfully!")
        except:
            print("Error adding book. Please try again.")
    
    def remove_book(self):
        """
        Remove book
        """
        title = input("Enter title of the book to remove: ")
        try:
            with open(self.filename, "r") as file:
                books = file.readlines()
            new_books = []
            for book in books:
                if not book.startswith(title + ","):
                    new_books.append(book)
            with open(self.filename, "w") as file:
                file.writelines(new_books)
            print("Book removed successfully.")
        except FileNotFoundError:
            print("No books found in the library.")
        except:
            print("Error removing book. Please try again.")
        
library = Library()

while True:
    print("\nLibrary Management System")
    print("1. List Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        library.list_books()
    elif choice == "2":
        library.add_book()
    elif choice == "3":
        library.remove_book()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        
        
        
        
        
        
        
        
        
        
        
        