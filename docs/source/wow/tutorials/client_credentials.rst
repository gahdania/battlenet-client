.. _backend workflow:


Client Credential Workflow
==========================

Simply instantiate the WoWClient with the following parameters.  When using python-decouple, you only
will need to supply the REGION.

#. REGION: the region for the API or use one of the :ref:`constants<Constants Source>`.

   - Examples of direct usage: us, kr, eu, tw, cn
   - Examples of constant usage: UNITED_STATES, KOREA, EUROPE, TAIWAN, CHINA

#. RELEASE: the release of the game to use.  Defaults to retail version of the game if not provided.

   - retail (default)
   - classic1x (Game Version 1.x Vanilla Classic)
   - classic (Game Version 2.x TBC Classic)

#. CLIENT_ID: the client ID
#. CLIENT_SECRET: the client secret

   - Both the client ID and secret are provided in the `API Access`_
   - The client tries to use these parameters if provided
   - The client then tries to uses the variables CLIENT_ID, CLIENT_SECRET inside the .env
     (See env.sample for more)

Example
-------

.. code-block:: python3

    > from wow_api.client import WoWClient
    > client = WoWClient(<REGION>, release=<RELEASE>, client_id=<CLIENT_ID>, client_secret=<CLIENT_SECRET>)
    # next make the call client.(api_module).(api_method)
    > client.playable_class.playable_class(client, <locale>, 7)

    # returns the data for shamans
    {'_links': {'self': {'href': 'https://us.api.blizzard.com/data/wow/playable-class/...


See the :ref:`WoWClient Source<Client Source>` for the complete list of methods available for use.



.. _API Access: https://develop.battle.net/access/clients
