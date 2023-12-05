import os
from lib.database_connection import get_flask_database_connection
from lib.book_repository import BookRepository
from lib.book import Book
from flask import Flask, request


# Create a new Flask app
app = Flask(__name__)


# == Your Routes Here ==
@app.route('/allbooks', methods=['GET'])
def get_all_books():
    connection = get_flask_database_connection(app)               
    repository = BookRepository(connection)                        
    books = repository.all()
    book_strings = [f"{book}" for book in books]
    return "\n".join(book_strings)

@app.route('/allbooks/<id>')
def get_single_books(id):
    connection = get_flask_database_connection(app)               
    repository = BookRepository(connection)                        
    book = repository.find(id)
    return str(book)

@app.route('/allbooks', methods=['POST'])
def post_books():
    connection = get_flask_database_connection(app)               
    repository = BookRepository(connection)
    title = request.form['title']
    author_name = request.form['author_name']
    book = Book(None, title, author_name)
    repository.create(book)
    return "Book created successfully."

@app.route('/allbooks/<id>', methods=['DELETE'])
def delete_books(id):
    connection = get_flask_database_connection(app)               
    repository = BookRepository(connection)
    repository.delete(id)
    return "Book deleted successfully."

@app.route('/submit', methods=['POST'])
def hello():
    name = request.form['name']
    message = request.form['message']
    return f"Thanks {name}, you sent this message: '{message}'"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"I am waving at {name}"



@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowels = "aeiouAEIOU"
    count_vowels = 0
    for char in text:
        if char in vowels:
            count_vowels += 1

    return f'There are {count_vowels} vowels in "{text}"'

# # Request:
# POST http://localhost:5001/sort-names

# # With body parameters:
# names=Joe,Alice,Zoe,Julia,Kieran

# # Expected response (sorted list of names):
# Alice,Joe,Julia,Kieran,Zoe
@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names']
    if names == '':
        return "There aren't any names to sort."
    new_names = names.split(", ")
    sorted_names = sorted(new_names)
    return ', '.join(sorted_names)


# # This route should return a list of pre-defined names, plus the name given.
@app.route('/names', methods=['GET'])
def add_names():
    add = request.args['add']
    if add == '':
        return "Julia, Alice, Karim"
    return f"Julia, Alice, Karim, {add}"




# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

