from flask import Blueprint, request, jsonify

# Define the blueprint
api = Blueprint('api', __name__)

# we create Dummy list to represent books
books = []
@api.route('/test', methods=['GET'])
def test_route():
    return "Flask is running correctly!"


# here is POST route to add a new book
@api.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    genre = data.get('genre')
    book = {
        'id': len(books) + 1,  # Simple auto-increment for book ID
        'title': title,
        'author': author,
        'genre': genre
    }
    books.append(book)
    return jsonify(book), 201  # Return the new book with status code 201 (created)

# GET route to get all books
@api.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200  # Return all books with status code 200
