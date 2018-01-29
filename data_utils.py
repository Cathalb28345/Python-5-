# import DBcm

# config = {

#   place working sql here 
#
#
# }


import pymongo


def add_to_scores(name, score, word, list_of_words) -> None:
    """Add the name and its associated score to the database, as well
       as the word (which was the sourseword), and also the list of
       words that the user got right."""
    score = {
        'name': name,
        'score': score,
        'sourceword': word,
        'words': list_of_words,
    }
    client = pymongo.MongoClient()
    db = client['leadersDB']
    c = db['leaderboard']
    c.insert_one(score)


def get_sorted_leaderboard() -> list:
    """Return a sorted list of tuples - this is the leaderboard."""
    client = pymongo.MongoClient()
    db = client['leadersDB']
    c = db['leaderboard']
    results = []
    for s in c.find().sort('score', pymongo.ASCENDING):
        results.append( ( s['score'], s['name'], s['sourceword'], s['words'] ) )
    return results
