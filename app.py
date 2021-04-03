from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
# decorator for routes that should be accessible only by logged in users
from auth_decorator import login_required

app = Flask(__name__)
app.secret_key = '!secret'
app.config.from_object('config')

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@app.route('/')
@login_required
def homepage():
    email = dict(session)['profile']['email']
    return render_template('home.html', user=email)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


#@app.route('/auth')
"""
    def auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    session['user'] = user
    return redirect('/')
    """
@app.route('/auth')
def auth():
    #google = oauth.create_client('google')  # create the google oauth client
    token = oauth.google.authorize_access_token()  # Access token from google (needed to get user info)
    #resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    #user_info = resp.json()
    user = oauth.google.parse_id_token(token)  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user
    #session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/')

@app.route('/logout')
def logout():
    #session.pop('user', None)
    #return redirect('/')
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')