.. _Introduction:

Introduction
============

The Battle.net REST API wrappers is package to make interfacing with the Battle.net API much easier.  It allows you,
the developer, to focus on writing your scripts without needing to worry about the boiler plate code.

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

This client uses two flows to help the developer focus on the tasks at hand.  The first is the OAuth credential client
flow, which uses just the developer's client ID and secret to authenticate with the BNET API.  The other is the
OAuth authorization code flow.  This one uses a combination of the developer's client ID and secret, as well as the
user's authorization with Blizzard, to allow access to the those particular endpoints.  The examples below are from the
wow branch of the package.  The other games' endpoints work in the same way.

Examples
--------

Oauth Credential Client Flow Example:

.. code-block:: python3

   > from battlenet_client import wow
   > client = wow.WoWClient(<region>, release=<release>, client_id=<client_id>, client_secret=<client_secret>)
   > client.playable_class.playable_class(<locale>, <class id>)


Oauth Authorization Code Flow Example:

.. code-block:: python3

   > from battlenet_client import wow
   > client = wow.WoWClient(<region>, scope=['wow.profile',], redirect_uri=<redirect_uri>, release=<release>,
                            client_id=<client_id>, client_secret=<client_secret>)
   > redirect(client.authorization_url())
   > client.account.account_profile_summary('en_US')
   {"_links": {"self": {"href": "https://us.api.blizzard.com/profile/user/wow?namespace=profile-us"}, ...

.. note::
   The Oauth authorization code flow will also work for the API endpoints that works with the credential code flow
   without the need to create a credential code flow client instance.
