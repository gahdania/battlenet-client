.. image:: https://img.shields.io/pypi/v/battlenet-client.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/battlenet-client.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/battlenet-client

.. image:: https://github.com/gahdania/battlenet-client/actions/workflows/tests.yaml/badge.svg?branch=v3.0.0
   :target: https://github.com/gahdania/battlenet-client/actions?query=workflow%3A%22Tests%22
   :alt: tests

.. image:: https://readthedocs.org/projects/battlenet-client/badge/?version=latest
   :target: https://battlenet-client.readthedocs.io/en/latest/?badge=latest

# BattleNet Clients
BattleNet Clients provide a uniform interface for Blizzard's Battle.net Developer Rest Application Programming
Interface (BNET Rest API)

## Installation

Windows, OS X & Linux:

    pip install battlenet_client

## Clone
Clone the latest version: https://github.com/gahdania/battlenet-client.git

## Usage Example

.. code-block:: python3

    > from battlenet_client.wow.game_data import achievement_category
    > achievement_category('us', category_id=81)
    # ('https://us.api.blizzard.com/data/wow/achievement-category/81', {'locale': None, 'namespace': 'static-us'})


For more information, please see the `readthedocs.io`_ page

## Release History
Please change log for complete history

## Meta

David "Gahd" Couples: `@gahdania <twitter>`_ / `Gahd on Twitch <twitch>`_ / `Email <gahdania@gahd.io>`_


Distributed under the GPL v3+ license. See ``LICENSE`` for more information.

`Battle.net Client on GitHub <github>`_

## Contributing

1. Create a `fork`_ from the project
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


.. _twitter: https://twitter.com/gahdania
.. _twitch: https://www.twitch.tv/gahd
.. _github: https://gitlab.com/battlenet1/battlenet-client
.. _fork: https://github.com/login?return_to=%2Fgahdania%2Fbattlenet-client
.. _readthedocs.io: https://battlenet-client.readthedocs.io/en/latest/
