class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def get_age(self):
        """Return the age of the book in years."""
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()}, File Size: {self.file_size} MB"