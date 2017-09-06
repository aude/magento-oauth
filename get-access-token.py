# script to negotiate an OAuth access token from Magento, to use with Magento REST API

from requests_oauthlib import OAuth1Session

client_key    = input('Consumer Key: ')
client_secret = input('Consumer Secret: ')

base_url      = input('Magento URL: ')

request_token_url      = base_url + '/oauth/initiate'
authorization_base_url = base_url + '/admin/oauth_authorize'
access_token_url       = base_url + '/oauth/token'

callback_url  = base_url

# initiate OAuth 1 session
magento = OAuth1Session(client_key,
                        client_secret = client_secret,
                        callback_uri = callback_url)

# get request token
request_token = magento.fetch_request_token(request_token_url)

# the user must verify Magento-side
authorization_url = magento.authorization_url(authorization_base_url)
print('Please go here and authorize: ' + authorization_url)

# get the authorization information we need
redirect_response = input('Paste the full URL you were redirected to here: ')
magento.parse_authorization_response(redirect_response)

# get the permanent access token
access_token = magento.fetch_access_token(access_token_url)

print('OAuth Access Token: ' + access_token['oauth_token'])
print('OAuth Access Token Secret: ' + access_token['oauth_token_secret'])
