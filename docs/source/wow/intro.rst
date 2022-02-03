.. _Introduction:

Introduction
============

The World of Warcraft API wrappers is package to make interfacing with the Battle.net API much easier.  It allows you,
the developer, to focus on writing your scripts without needing to worry about the boiler plate code.  This module
depends on the `BattleNet Client <https://gitlab.com/battlenet1/battlenet-client>`_

Installation
============
To install this package is use your favorite python package installation utility, or use git


For Windows, OS X, and Linux
----------------------------

.. code-block:: bash

   pip install wow_api

Using GIT
---------

.. code-block:: bash

   git clone https://gitlab.com/battlenet1/wow_api.git

Usage
=====

There are two modes when using the client.  The first is use client credentials.  The other using is use an
authorization code to access API end points.

Client Credential Flow
----------------------


.. code-block:: python3

   from wow_api.client import WoWClient

   # set up the client first
   client = WoWClient('<region tag>', client_id='<CLIENT_ID>', client_secret='<CLIENT_SECRET>')

   # next make the call client.(api_name).(api_method)
   data = client.achievement.achievement(<preferred locale>, <achievement id>)

Authorization Code Flow
-----------------------

Below is a typical example of using the authorization code flow.

.. warning:: Reminder:  this requires the code to operate within a web server

.. code-block:: python3

   from wow_api.client import WoWClient
   from wow_api.profile.account_profile import account_profile_summary
   # <region_tag>: region for the user, ie us, eu, tw, kr or cn
   # <scope>: the scope need to for your site
   # <redirect>: the URI where you want users to return after successfully authenticating with Battle.net
   # <client ID>: the client ID from the Developer Portal
   # <client secret>: the client secret from the Developer Portal
   client = WoWClient(<region tag>, scope=[wow.profile, ], redirect_uri=<REDIRECT URL>, client_id=<CLIENT ID>,
                      client_secret=<CLIENT SECRET>)

   # redirect user to the url from client.authorization_url()

   # user goes to Blizzard's authentication site on battle.net and successfully logs in
   # Battle.net redirects the user to redirect_uri
   client.account.account_profile_summary(<preferred locale>)
