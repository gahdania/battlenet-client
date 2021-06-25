.. _credential-workflow-tutorial:

:ref:`Home <home-page>` / :ref:`Tutorials Home <tutorials-index>`

Credential Authorization Workflow
=================================

First of all, the client authorization workflow is **the** most commonly used workflow
by the Battle.Net REST API.

As mentioned in the :ref:`usage summary <usage>` page, you will need a developer account. As well as having a client configured in the portal.

As you will see in the below :ref:`example <credential-workflow-example>`, you will need to first import the BattleNetClient class, then
instantiate it.

.. _credential-workflow-example:

.. code-block:: python3

    # Import it
    from battlenet_client import BattleNetClient

    # Instantiate it
    client = BattleNetClient('<region abbreviation>', client_id='<client id>', client_secret='<client_secret>')

    # request the data from it
    return client.request('<method>', '<api endpoint uri>', locale='<locale preferred>', namespace='<namespace>')

That is it. Again, there are other packages that work with this class, allowing you to focus on the more important parts of your project

See Also: :ref:`User Authorization Workflow Tutorial <authentication-workflow-tutorial>`

:ref:`Home <home-page>` / :ref:`Tutorials Home <tutorials-index>`

.. include:: ../footer.rst