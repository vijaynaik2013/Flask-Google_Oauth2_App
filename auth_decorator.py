from flask import session
from functools import wraps
from flask import render_template, redirect

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)
        # You would add a check here and use the user id or something to fetch
        # the other data for that user/check if they exist
        if user:
            return f(*args, **kwargs)
        #return "You ain't logged in, please use url http://127.0.0.1:5000/login to get authenticated!"
        return render_template('logout.html', user = user)
    return decorated_function