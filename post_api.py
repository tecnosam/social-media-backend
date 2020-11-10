import os, sys
import json
from pher import Strap
import time

def create_post( caption, uid, file = "", filetype = "blank" ):
    pid = Strap.pid( uid, caption )
    data = {
        'uid': uid,
        "caption": caption,
        'file': file,
        "filetype": filetype,
        "likes": [],
        "comments": {},
        "saves": [],
        "pid": pid,
        'date-posted': time.time()
    }

    json.dump( data, open( f"data/posts/{pid}.json", "w" ) )

    data = json.load( open( f"data/users/{uid}.json" ) )
    data['posts'].append( pid )
    json.dump( data, open( f"data/users/{uid}.json", "w" ) )

    return True

def delete_post( uid, pid ):

    dat = json.load( open( f"data/users/{uid}.json", "r" ) )
    dat['posts'].remove( pid )
    json.dump( dat, open( f"data/users/{uid}.json", "w" ) )

    return os.remove( f"data/posts/{pid}.json" )

def like ( uid, pid ):
    post = json.load( open( f"data/posts/{pid}.json", "r" ) )
    if ( uid not in post[ 'likes' ] ):
        post[ 'likes' ].append( uid )
    else:
        post[ 'likes' ].remove( uid )
    json.dump( post, open( f"data/posts/{pid}.json", "w" ) )

    user = json.load( open( f"data/users/{uid}.json", "r" ) )
    if ( pid not in user[ 'likes' ] ):
        user[ 'likes' ].append( pid )
    else:
        user['likes'].remove( pid )
    json.dump( user, open( f"data/users/{uid}.json", "w" ) )

    return True

def save ( uid, pid ):
    post = json.load( open( f"data/posts/{pid}.json", "r" ) )

    if ( uid not in post['saves'] ):
        post[ 'saves' ].append( uid )
    else:
        post['saves'].remove( uid )

    json.dump( post, open( f"data/posts/{pid}.json", "w" ) )

    user = json.load( open( f"data/users/{uid}.json", "r" ) )

    if ( pid not in user['saves'] ):
        user[ 'saves' ].append( pid )
    else:
        user[ 'saves' ].remove( pid )

    json.dump( user, open( f"data/users/{uid}.json", "w" ) )

    return True

def comment ( uid, pid, comment ):
    post = json.load( open( f"data/posts/{pid}.json", "r" ) )
    if ( uid in post[ 'comments' ] ):
        post[ 'comments' ][ uid ].append( comment )
    else:
        post[ 'comments' ][ uid ] = [ comment ]
    json.dump( post, open( f"data/posts/{pid}.json", "w" ) )

    user = json.load( open( f"data/users/{uid}.json", "r" ) )
    if ( pid in user['comments'] ):
        user[ 'comments' ][ pid ].append( comment )
    else:
        user[ 'comments' ][ pid ] = [ comment ]
    json.dump( user, open( f"data/users/{uid}.json", "w" ) )

    return True

def edit_caption( uid, pid, caption ):
    data = json.load( open( f"data/posts/{pid}.json", "r" ) )
    if (data['uid'] == uid):
        data['caption'] = caption
    else:
        return False
    json.dump( data, open( f"data/posts/{pid}.json", "w" ) )
    return True

def get_posts():
    return [
        json.load( open( f"data/posts/{i}", "r" ) ) \
        for i in os.listdir( "data/posts" )
    ]


# print(create_post( "I love ripped Jeans", "286b3124661c7e480b2093dbe309ac3e" ))

# print( delete_post( "d07bdc71dc1e7e383f7b7bc7d669233d", "a8c4d201486d678ff546e28d6dd86544" ) )

# print( like( "286b3124661c7e480b2093dbe309ac3e", "b79503d4870741bd5b74bfd832cf1041" ) )

# print( save( "286b3124661c7e480b2093dbe309ac3e", "b79503d4870741bd5b74bfd832cf1041" ) )

# print( comment( "286b3124661c7e480b2093dbe309ac3e", "b79503d4870741bd5b74bfd832cf1041", "nice" ) )
