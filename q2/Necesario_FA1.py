# hi sir, sakto rani?

class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    def set_number_of_pages(self, pages):
        if pages <= 0:
            print("The number of pages must be positive")
        else:
            self.__number_of_pages = pages

    def display_info(self):
        super().display_info()
        print("Number of pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    def set_issue_number(self, issue):
        if issue <= 0:
            print("The issue number must be positive")
        else:
            self.__issue_number = issue

    def display_info(self):
        super().display_info()
        print("Issue number:", self.__issue_number)


publication1 = Publication("Library Science", "John Smith")
publication2 = Publication("Learning Python", "Mary Cruz")

book1 = Book("Introduction to Programming", "Alice Brown", 250)
book2 = Book("Object-Oriented Programming", "David Lee", 320)

magazine1 = Magazine("Science Today", "Peter Santos", 1)
magazine2 = Magazine("Technology Weekly", "Anna Reyes", 5)


print("=== PUBLICATIONS ===")
publication1.display_info()
print()
publication2.display_info()

print("\n=== BOOKS ===")
book1.display_info()
print()
book2.display_info()

print("\n=== MAGAZINES ===")
magazine1.display_info()
print()
magazine2.display_info()
