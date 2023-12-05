

# Tests for your routes go here

# Test-drive a route GET/artists which will return a list of artists
# # Request:
# GET /artists

def test_all_artists(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"


# Test-drive a route POST /artists, which creates a new artist in the database. 
# Your test should verify the new artist is returned in the response of GET /artists.
# request: POST /artists
def test_create_artist(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    post_response = web_client.post("/artists", data={'name': "The Beatles", "genre": 'Rock'})
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone, The Beatles"

# # Request:
# POST /albums

# # With body parameters:
# title=Voyage
# release_year=2022
# artist_id=2

def test_create_album(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    post_response = web_client.post("/albums", data={'title': "Voyage", "release_year": '2022', "artist_id": '5'})
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)\n" \
        "Album(13, Voyage, 2022, 5)"

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
