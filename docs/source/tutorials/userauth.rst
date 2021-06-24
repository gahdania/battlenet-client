.. _authentication-workflow-tutorial:

:ref:`Home <home-page>` / :ref:`Tutorials Home <tutorials-index>`

User Authentication Workflow
============================
The User Authentication Workflow is a bit different from the :ref:`credential authentication workflow <credential-workflow-tutorial>`

The one additional requirement is that there a web server the user will be returning to after he/she has gone through
the authentication process with Blizzard.  The other is we define the scope, or permissions we want to have

Before we get into the details, here is a brief breakdown of the process for this workflow

#. The user visits the website you are building
#. The user then clicks on a link to authenticate with Battle.Net
#. The user authenticates with Battle.Net
#. Battle.net then redirects the user to your site to a location of your choosing (redirect_uri) called a callback,
   after successfully authenticating with Blizzard
#. The user accesses the endpoints that require the User Authentication Workflow

For the rest of these tutorials, the location the user is going to be returning to is a callback or redirection URI.

.. _authentication-workflow-example:

.. code-block:: python3

    from battlenet_client import BattleNetClient
    client = BattleNetClient('<region abbreviation>', '<scope of request>', '<redirection uri>', client_id='<CLIENT ID>', client_secret='<CLIENT_SECRET>')

    # from the html generator part of the project
    # generate a link or redirect the user to authenticate the user with Battle.Net
    redirect(client.authorization_url)

    # The user successfully authenticates with Battle.Net and gets redirected back
    # to the redirection URI you supplied
    # then like the credential workflow we call the request to the API
    # request the data via a GET as below
    client.get('<endpoint uri>', locale='<locale requested>', namespace='<namespace>')

    # or as a post
    client.post('<endpoint uri>', locale='<locale requested>', namespace='<namespace>')

See Also: :ref:`Credential Workflow Tutorial <credential-workflow-tutorial>`

:ref:`Home <home-page>` / :ref:`Tutorials Home <tutorials-index>`