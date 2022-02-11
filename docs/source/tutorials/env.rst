.. _env:

Using Python-Decouple
=====================

In the packages, I have incorporated the use of Python Decouple.  This module allows the shifting of sensitive data
away from the scripts, such as the client ID and secret.  To use it, simply copy the env.sample file to the base
appropriate location as ".env"

Change <CLIENT_ID> and <CLIENT_SECRET> to to appropriate values indicated by `API Access`_.  You may need to click "Show
Secret" to view the client secret

For the example below, the client ID will be 'MY CLIENT ID' and the the secret will be 'A really bad secret'

in the env.sample (now copied and renamed to .env)

.. code-block:: ini

   CLIENT_ID=MY CLIENT ID
   CLIENT_SECRET=A really bad secret

With the above in the .env file, then you can instantiate the client like the following

.. code-block:: python3

   from battlenet_client import wow
   client = wow.WoWClient('us')

.. _API Access: https://develop.battle.net/access/clients
