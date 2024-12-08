class Book:
    def __init__(self, id, title, author, genre, available=True):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Member {self.name}>"
