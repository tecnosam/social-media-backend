from flask import *
import account_api, post_api

app = Flask( __name__ )

# TODO: Add notifications feature
# TODO: test with postman
# TODO: imrpove error handling

# account routes
@app.route("/signup", methods = ['POST'])
def signup():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']

    return jsonify( account_api.create_account( email, username, password, name ) )

@app.route( "/login", methods = ['POST'] )
def login():
    token = request.form['token']
    password = request.form['password']

    return jsonify( account_api.login( token, password ) )

@app.route("/edit-account", methods = ['POST'])
def edit_acct():
    uid = request.headers.get( "uid" )
    node = request.form['node']
    val = request.form['val']
    return jsonify( account_api.edit( uid, node, val ) )

@app.route( "/follow", methods = ['POST'] )
def follow():
    uid = request.headers.get( "uid" )
    tpuid = request.form['uid'] # uid of persion you want to follow

    return jsonify( account_api.follow( uid, tpuid ) )

@app.route("/delete-account", methods = ['POST'])
def del_acct():
    uid = request.headers.get( "uid" )

    return jsonify( account_api.delete( uid ) )

# endof session

# posts
@app.route("/create-post", methods = ['POST'])
def create_post():
    uid = request.headers.get( "uid" )
    caption = request.form['caption']
    if 'file' in request.files:
        file = request.files['file']
        fn = secure_filename( file.filename )
        file.save( f"data/uploads/{uid}-{time.time()}-{fn}" )
        file = fn
        filetype = request.form['filetype']
    else:
        file = ""
        filetype = "blank"

    return jsonify( post_api.create_post( caption, uid, file, filetype ) )

@app.route("/delete-post", methods = ['POST'])
def del_post():
    uid = request.headers.get( "uid" )
    pid = request.form['pid']

    return jsonify( post_api.delete_post( pid ) )

@app.route( "/like-post", methods = ['POST'] )
def like():
    uid = request.headers.get()
    pid = request.form['pid']

    return jsonify( post_api.like( uid, pid ) )

@app.route( "/save-post", methods = ['POST'] )
def save():
    uid = request.headers.get()
    pid = request.form['pid']

    return jsonify( post_api.save( uid, pid ) )

@app.route( "/comment-post", methods = ['POST'] )
def comment():
    uid = request.headers.get()
    pid = request.form['pid']
    comment = request.form[ 'comment' ]

    return jsonify( post_api.comment( uid, pid, comment ) )

@app.route( "/edit-caption", methods = ['POST'] )
def edit_caption():
    uid = request.headers.get()
    pid = request.form['pid']
    caption = request.form[ 'caption' ]

    return jsonify( post_api.edit_caption( uid, pid, caption ) )

@app.route("/posts", methods = ['GET', 'POST'])
def posts():
    return jsonify( post_api.get_posts() )

if __name__ == '__main__':
    app.run( debug = True )
