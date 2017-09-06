# example script to query the Magento REST API

from requests_oauthlib import OAuth1Session

client_key    = '57e27934885e98600dc22bfc436fd280'
client_secret = 'c11ba1c78d2dcdaf8719b712d00a4c9d'
access_token  = '72c9831bb2e6d6131526d61500255970'
access_secret = 'c0104df08c6197b8d2bc86c3da1cca13'

base_url      = 'http://customer.com'

magento = OAuth1Session(client_key,
                        client_secret = client_secret,
                        resource_owner_key = access_token,
                        resource_owner_secret = access_secret)

result = magento.get(base_url + '/api/rest/products')

print(result.text)
