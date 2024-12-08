books = []
members = []
# we Define the list types


# here is a Function to create a new book with typed parameters and return type
def create_book(title, author, genre):
    book_id = len(books) + 1
    book = Book(book_id, title, author, genre)
    books.append(book)
    return book

# Now create Function to new member with typed parameters and return type
def create_member(name, email):
    member_id = len(members) + 1
    member = Member(member_id, name, email)
    members.append(member)
    return member
