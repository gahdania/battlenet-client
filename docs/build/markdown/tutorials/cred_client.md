# Credential Authorization Workflow

**NOTE**:
* Note that you can still use the user authorization client, with the endpoints that accept the client credentials
as well.


* Any OAuth v2 or OpenID Connect client will work with the endpoints.  The ones contained in the package are for
convenience


* Authorization Code Flow will be the most common for user authentication, while credential client code flow
will be for backend work, such as maintaining the persistent data, such as playable classes.

First of all, the client authorization workflow is **the** most commonly used workflow
by the Battle.Net REST API.

As mentioned in the [usage summary](usage-summary) page, you will need a developer account. As well as having a client configured in the portal.

As you will see in the below [example](credential-workflow-example), you will need to first import the BattleNetClient class, then
instantiate it.

## Example

```
# Import it
from battlenet_client.clients import CredentialClient
from battlenet_client import wow

# Instantiate it
client = CredentialClient('<region>', <client id>, <client_secret>)

# request the data using it
return wow.Achievement.achievement_category(client, '<region abbreviation>', category_id=81, locale='<locale>')
```

That is it. Again, there are other packages that work with this class, allowing you to focus on the more important parts of your project

See Also: [User Authorization Workflow Tutorial](authentication-workflow-tutorial)
