from datetime import datetime


class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False
        self.checked_out_by = None
        self.checkout_date = None

    def check_out(self, borrower):
        if not self.checked_out:
            self.checked_out = True
            self.checked_out_by = borrower
            self.checkout_date = datetime.now()
            print(f"{self.title} has been checked out by {borrower}.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            self.checked_out_by = None
            self.checkout_date = None
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already in the library.")

    def display_info(self):
        status = "Available" if not self.checked_out else "Checked out"
        print(
            f"Title: {self.title}\nAuthor: {self.author}\nItem ID: {self.item_id}\nStatus: {status}"
        )


class Book(LibraryItem):
    def __init__(self, title, author, item_id, isbn):
        super().__init__(title, author, item_id)
        self.isbn = isbn

    def display_info(self):
        super().display_info()
        print(f"ISBN: {self.isbn}")


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}\nDuration: {self.duration} minutes")


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number):
        super().__init__(title, publisher, item_id)
        self.publisher = publisher
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Publisher: {self.publisher}\nIssue Number: {self.issue_number}")


# Create new items with different data
book = Book("1984", "George Orwell", "002", "978-0451524935")
dvd = DVD("The Matrix", "Lana Wachowski, Lilly Wachowski", "102", 136)
magazine = Magazine(
    "Time", "Time Inc.", "202", "Vol. 198, No. 12"
)


book.display_info()
print()
dvd.display_info()
print()
magazine.display_info()
print()


book.check_out("Michael")
dvd.return_item()
magazine.check_out("Sophia")
book.check_out("Oliver")
