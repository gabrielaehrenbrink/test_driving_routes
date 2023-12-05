# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

def test_get_wave_with_argument(web_client):
    response = web_client.get("/wave?name=Dana")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "I am waving at Dana"

def test_post_submit_with_arguments(web_client):
    response = web_client.post('/submit', data={ "name": "Dana", "message": "hello"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Thanks Dana, you sent this message: 'hello'"


"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


# EXAMPLE - create example tests "sort names"

# POST /sort-names Joe, Alice, Zoe, Julia, Kieran
# """
# Expected response (sorted list of names):
# Alice,Joe,Julia,Kieran,Zoe
# """
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe, Alice, Zoe, Julia, Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Joe, Julia, Kieran, Zoe"

# # POST /sort-names alice, zoe
# """
# Expected response (sorted list of names): alice, zoe
# """
def test_post_sort_two_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'zoe, alice'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "alice, zoe"

# POST /sort-names
# """
# There aren't any names to sort.
# """
def test_post_sort_zero_names(web_client):
    response = web_client.post('/sort-names', data={'names': ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "There aren't any names to sort."



# # Request:
# GET /names?add=Eddie

# # This route should return a list of pre-defined names, plus the name given.

# # Expected response (2OO OK):
# Julia, Alice, Karim, Eddie

# test add one name: should return a list of pre-defined names, plus the name given
def test_add_one_name(web_client):
    response = web_client.get("/names?add=Eddie")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'


# test add no names: should return a list of pre-defined names
def test_add_zero_name(web_client):
    response = web_client.get("/names?add=")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim'


# test add multiple names: should return a list of pre-defined names, plus the given names
def test_add_zero_name(web_client):
    response = web_client.get("/names?add=Eddie, Maria")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie, Maria'



def test_get_all_books(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.get('/allbooks')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)"


# get /books/<id>

def test_get_single_books(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.get('/allbooks/1')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Book(1, Invisible Cities, Italo Calvino)" 


def test_create_new_books(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.post('/allbooks', data={
        'title': 'Out of the Crisis',
        'author_name': 'W Edwards Deming'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Book created successfully."

    response = web_client.get('/allbooks')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)\n" \
        "Book(6, Out of the Crisis, W Edwards Deming)"
    
def test_delete_book(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.delete('/allbooks/2')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Book deleted successfully."

    response = web_client.get('/allbooks')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)"