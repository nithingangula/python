class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")


class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        super().display_info()
        print(f"Pages : {self.pages}")
        print("-" * 30)


class EBook(LibraryItem):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.__file_size = file_size  # Encapsulation

    def get_file_size(self):
        return self.__file_size

    def display_info(self):
        super().display_info()
        print(f"File Size: {self.get_file_size()} MB")
        print("-" * 30)


def show_library(items):
    print("\n===== LIBRARY =====")
    for item in items:
        item.display_info()


book1 = Book("Python Basics", "Nithin", 250)
book2 = Book("Data Structures", "John", 420)
ebook1 = EBook("Agentic AI Guide", "OpenAI", 18)

library = [book1, book2, ebook1]

show_library(library)