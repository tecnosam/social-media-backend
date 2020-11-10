import json, os, sys
from pher import Strap
from hashlib import md5

def create_account(email, username, password, name):
    if  not ( (login( username )[0] == None) and ( login( email )[0] == None ) ):
        return False, "User Already Exists"
    uid = Strap.uid( email, username )
    password = md5( password.encode() ).hexdigest()

    data = {
        'uid': uid,
        'email': email,
        'username': username,
        'password': password,
        'name': name,
        'avatar': "profile.jpg",
        "bio": "",
        "followers": [],
        "following": [],
        "posts": [],
        "saves": [],
        "likes": [],
        "comments": {},
        "notifications": []
    }
    file = open( f"data/users/{uid}.json", "w" )
    json.dump( data, file )
    return True, "Successful"

def login( token, password = "" ):
    _password = md5( password.encode() ).hexdigest()
    for i in os.listdir( "data/users" ):
        file = open( f"data/users/{i}", "r" )
        data = json.load( file )
        if ( ( data['username'] == token ) or ( data['email'] == token ) ):
            # print(token)
            if ( _password == data['password'] ):
                del file
                data['password'] = password
                return True, data
            else:
                # print("dick")
                return False, "Invalid Password"
        del data
        del file
    return None, "User not found"

def edit( uid, node, val ):
    if ( node == 'password' ):
        val = md5( val.encode() ).hexdigest()
    if ( node in ['email', 'username'] ):
        if ( login( node )[0] != None ):
            return False, f"{node} is taken by another user"

    file = open( f"data/users/{uid}.json", "r+" )
    data = json.load( file )
    data[ node ] = val
    file = open( f"data/users/{uid}.json", "w" )
    return json.dump( data, file ), "yay"

def follow(uid, tpuid):
    file = open( f"data/users/{uid}.json", "r+" )

    data = json.load( file )
    data['following'].append( tpuid )
    file = open( f"data/users/{uid}.json", "w" )
    json.dump( data, file )

    file.close(); file = open( f"data/users/{tpuid}.json", "r+" )

    data = json.load( file )
    data['followers'].append( uid )
    file = open( f"data/users/{tpuid}.json", "w" )
    return json.dump( data, file )

def delete( uid ):
    dat = json.load( open( f"data/users/{uid}.json", "r" ) )
    for pid in dat['posts']:
        os.remove( f"data/posts/{pid}.json" )
    return os.remove( f"data/users/{uid}.json" )

# print( delete( "286b3124661c7e480b2093dbe309ac3e" ) )
# print( create_account( "ikabolo59@gmail.com", "admin", "fish", "Abolo Samuel" ) )
# print( login( "ikabolo59@gmail.com", "fish" ) )
# print( edit( "d07bdc71dc1e7e383f7b7bc7d669233d", "password", "rice" ) )
# print( edit( "d07bdc71dc1e7e383f7b7bc7d669233d", "bio", "CEO of IceCoffee" ) )
# print( edit( "d07bdc71dc1e7e383f7b7bc7d669233d", "avatar", "CEO.png" ) )
# print( create_account( "ikisaac59@gmail.com", "ceo", "fish", "Abolo Isaac" ) )
# print( follow( '286b3124661c7e480b2093dbe309ac3e', 'd07bdc71dc1e7e383f7b7bc7d669233d' ) )
