# Install following packages
pip install -U Flask Authlib requests

# Create OAUTH2 Client Credentials to be entered in Config.py file:
1. Login to https://console.cloud.google.com using your gmail credentials
2. Navigate to API & Services
3. Create "OAuth 2.0 Client IDs" by navigating to Credentials tab
4. Add URI's as below for respective tabs:
        - Authorized JavaScript origins --> http://127.0.0.1:5000
        - Authorized redirect URIs on seperate lines --> 
              - http://127.0.0.1:5000/auth
              - http://localhost:5000/auth
5. Post creation of the credentials, note down the Client ID and Client secret and copy these values in config.py file

# Starting Flask Application
1. Navigate to projects director
2. Execute command from command line - "flask run"
