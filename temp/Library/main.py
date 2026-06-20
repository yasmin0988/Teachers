from library import Library

#book_list = ["1984", "jane eyre", "pride and prejudice", "100 year of solitude"]
#Library.add_book("anna karennina", book_list)
#Library.remove_book("1984", book_list)
#Library.search_book("jane", book_list)
#Library.show_books(book_list)

books = input("Enter your books: ")
books_list = map(list, books.split(","))

if __name__ == "__main__":
    books = input("Enter your books: ")
    books_list = map(list, books.split(","))
    menu = {1:"Add book", 2:"Remove book", 3:"Search book", 4:"Show books"}
    choice = input(f"{menu}\nEnter your choice: ")

    match choice:
        case 1:
            new_book = input("Enter the new book: ")
            Library.add_book(new_book, books_list)
            print(books_list)

        case 2:
            removing_book = input("Enter the removing book: ")
            Library.remove_book(removing_book, books_list)
            print(books_list)

        case 3:
            searching_book = input("Enter the searching book: ")
            Library.search_book(searching_book, books_list)
            print(books_list)
        
        case 4:
            print(books_list)