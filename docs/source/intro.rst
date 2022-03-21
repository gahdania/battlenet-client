============
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

   pip install battlenet_client

Using GIT
---------

.. code-block:: bash

   git clone https://github.com/gahdania/battlenet-client.git


Usage
=====

The functions contained in this packages format the given parameters into a URL and a set of key/value pairs for the
parameter (query string) of the GET requests.  This package does not actually provide the communication between the
users and the Battle.net REST API

Examples
--------

The below example will generate the URL and parameter key/value pairs to retrieve the achievement category, using
the North America server

.. code-block:: python3

   > from battlenet_client.wow.game_data import achievement_category
   > achievement_category('us', category_id=81)
   # ('https://us.api.blizzard.com/data/wow/achievement-category/81', {'locale': None, 'namespace': 'static-us'})

Same as above but this time getting just the french localization for the achievement category

.. code-block:: python3

   > from battlenet_client.wow.game_data import achievement_category
   > achievement_category('us', category_id=81, locale='frfr')
   # ('https://us.api.blizzard.com/data/wow/achievement-category/81', {'locale': 'fr_FR', 'namespace': 'static-us'})

The developer would then provide the output of the functions to the client of their choice

Please see :ref:`Developer Portal Instructions` for further details
