=================================
Credential Authorization Workflow
=================================

First of all, the client authorization workflow is **the** most commonly used workflow
by the Battle.Net REST API.

As mentioned in the `usage summary <usage-summary>`_ page, you will need a developer account. As well as having a client configured in the portal.

As you will see in the below `example <credential-workflow-example>`_, you will need to first import the BattleNetClient class, then
instantiate it.

Example
-------

.. code-block:: python3

    # Import it
    from battlenet_client.client import BattleNetClient
    from battlenet_client.constants import UNITED_STATES, WOW

    # Instantiate it
    client = BattleNetClient(UNITED_STATES, WOW, <client id>, <client_secret>)

    # request the data from it
    return client.api_get('<api endpoint uri>', '<locale preferred>', headers={'Battlnet-Namespace': '<namespace>'})

That is it. Again, there are other packages that work with this class, allowing you to focus on the more important parts of your project

See Also: `User Authorization Workflow Tutorial <authentication-workflow-tutorial>`_
