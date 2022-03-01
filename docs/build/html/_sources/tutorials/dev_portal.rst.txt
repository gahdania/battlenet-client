=============================
Developer Portal Instructions
=============================

Here are the instructions for setting up a Developer Portal account, as well as getting things ready for your projects.
[#]_

Signing up for the developer portal
-----------------------------------

#. Go to the `Developer Portal Site <https://develop.battle.net>`_
#. In the upper right of the screen, click on the link called "My Account"
#. Click on "Log In"
#. Use the same log in username and password you do for the Battle.net Launcher or any of the Blizzard Games

Gather the Necessary Information
--------------------------------

#. Name of the Client (Has to be unique)
#. URL of your site where you want the users to return after successfully authenticating.
#. Base URL for your website
#. Statement about how you plan on using the data from the Developer Portal

Fill in the Information
-----------------------

#. Click on the "+ Create Client" on the right hand side of the screen
#. Under "Client Name", input the name.
#. Under "Redirect URLs" input the URL(s)
#. Under "Service URL" input the URL. [#]_
#. Under "Intended Use" input the use.
#. Once everything is satisfactory, the "Save" button will be highlighted.  Click "Save"

Get the Client ID and Secret
----------------------------
#. After you save, you are shown a page with all of the information you filled in.  At the top under "Credentials",
   you should have a string of characters over "Client ID".  That string of characters is the client ID, you will need
   for this package
#. Click on "SHOW SECRET" above "Client Secret".  This will show another string of characters, which is your client
   secret

.. warning:: All data retrieved, and entered in/on the site is the intellectual property of Activision/Blizzard

.. [#] The process is current as of 2020-May-03.  The form may change without notice.
.. [#] If you do not have a service URL yet, then click the check box under "Service URL".
   Remember to return to the portal and add the URL once you have it. Afterward you can click off the check box below
   "Service URL"
