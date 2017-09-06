Magento REST API OAuth helpers
==============================

A set of scripts to help using Magento's REST API authenticated through OAuth.

Requirements
------------

- Python 3.6

Installation
------------

    $ make

This will create a Python virtual environment in `.venv` and install the required Python libraries there.
Nothing is installed globally.

Get OAuth access token
----------------------

To connect to eg. the Magento REST API, you need to authenticate through OAuth.
To be authenticated through OAuth, you need an OAuth access token.
The access token needs to be negotiated and accepted by both client and server side,
and therefore involves a bit of back and forth between you and Magento.
The `get-access-token.py` script can help you get an access token.

    $ make get-access-token

Be sure to save your access token information! It is not recoverable.

Make API calls
--------------

Now that you've got your access token, you can make API calls.
The included `usage-example.py` script shows an example of how this can be done.

Further information on the Magento REST API and OAuth
------------------------------------------------

- http://inchoo.net/magento/magento-rest-and-oauth-intro/
- http://inchoo.net/magento/configure-magento-rest-and-oauth-settings/
- http://inchoo.net/magento/consuming-magento-rest-zend_oauth_consumer/
- https://stackoverflow.com/questions/28045800/how-to-use-postman-rest-client-with-magento-rest-api-with-oauth-how-to-get-toke
- https://youtu.be/tFYrq3d54Dc
- https://tools.ietf.org/html/rfc5849
