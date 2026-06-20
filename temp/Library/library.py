class Library:
    def __init__(self, title=str, author=str, books=list):
        self.title=title
        self.author=author
        self.books=books

    def add_book(title, books):
        books.append(title)

    def remove_book(title, books):
        books.remove(title)
    
    def search_book(title, books):
        for book in books:
            if book == title:
                print(f"{book} was found")

    def show_books(books):
        i=1
        for book in range(len(books)):
            print(f"{i}. {books[i-1]}\n")
            i += 1
        

