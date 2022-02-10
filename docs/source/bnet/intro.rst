Introduction
============

BattleNet Client was developed to provide a uniform access point for the other Battle.net projects that connect to
Blizzard's `Battle.net Developer Portal <https://develop.battle.net>`_. The other packages,
`WoW API <https://gitlab.com/battlenet1/wow-api>`_, `Hearthstone API <https://gitlab.com/battlenet1/heartstone-api>`_,
`Starcraft2 API <https://gitlab.com/battlenet1/starcraft2-api>`_ extends the Battle.Net Client for the respective game

Installation
============

To install the Battle.net Client package, all you have to do use your favorite python package installation utility, or use git

For Windows, OS X and Linux
---------------------------

.. code-block:: bash

   pip install battlenet-client

Using GIT
---------

.. code-block:: bash

   git clone https://gitlab.com/battlenet1/battlenet-client.git

Usage
=====

This package requires a developer portal account. For more information, please see the
`Developer Portal`_.  As for the regions and localizations that are available,
you can view that information at `Blizzard's Regionality, Partitions, and Localization`_

Client Credential Flow
----------------------

Below is a typical example in using the client credential flow.

.. code-block:: python3

   from battlenet_client.client import BattleNetClient
   from battlenet_client.constants import UNITED_STATES, WOW
   # <region_tag>: use the constant appropriate for your region
   # <client ID>: the client ID from the Developer Portal
   # <client secret>: the client secret from the Developer Portal
   client = BattleNetClient(UNITED_STATES, WOW, <client ID>, <client secret>)

   # <method>:  Typically use 'api_get' or 'api_post' depending on the API endpoint being reached
   # <api_uri>: The API endpoint URL w/o the scheme, or host
   # <locale>: the desired localization to use if something other than when the client was created
   # <namespace>: the namespace expected by the :api_uri:
   client.api_get(<api_uri>, <locale>, headers={'Battlenet-Namespace': <namespace>-<region_tag>})

Authorization Code Flow
-----------------------

.. _usage:

Below is a typical example of using the authorization code flow.

.. note:: Reminder:  this requires the code to operate within a web server

.. code-block:: python3

   from battlenet_client import BattleNetClient
   # <region_tag>: region for the user, ie us, eu, tw, kr or cn
   # <scope>: the scope need to for your site
   # <redirect>: the URI where you want users to return after successfully authenticating with Battle.net
   # <client ID>: the client ID from the Developer Portal
   # <client secret>: the client secret from the Developer Portal
   client = BattleNetClient(UNITED_STATES, WOW, <CLIENT ID>, <CLIENT SECRET>, scope=[wow.profile, ],
       redirect_uri=<REDIRECT URL>)
   redirect(client.authorization_url)

   # user goes to Blizzard's authentication site on battle.net and successfully logs in
   # Battle.net redirects the user to <redirect>
   # <method>:  Typically 'get' or 'post' with 'get' being the most frequent
   # <api_uri>: The API endpoint URL w/o the scheme, or host
   # <locale>: the desired localization to use
   # <namespace>: the namespace expected by the :api_uri:
   # for the endpoints that use the GET method
   client.api_get(<api_uri>, <locale>, headers={'Battlenet-Namespace': <namespace>-<region_tag>})
   # for the endpoints that use the POST method
   client.api_post(<api_uri>, <locale>, headers={'Battlenet-Namespace': <namespace>-<region_tag>})


For more detailed instructions please see the :ref:`tutorials index <tutorials-index>`

For a complete list of the classes, functions, and parameters go to :ref:`BattleNet Class Index <clients-code>`

To use the utility functions, simply import the required ones and pass then call them as any normal function

Utility Function Examples
-------------------------

.. code-block:: python3

    from battlenet_client.util import currency_convertor, slugify, localize
    print(currency_convertor(4912309))
    # {'gold': 491, 'silver': 23, 'copper': 9}

    print(slugify("Zul'jin")
    # 'zuljin'

    print(localize("enus")
    # 'en_US'

.. include:: footer.rst

.. _Blizzard's Regionality, Partitions, and Localization: https://develop.battle.net/documentation/guides/regionality-partitions-and-localization
.. _Developer Portal: https://develop.battle.net
