"""This module contains all of the methods for accessing account related
information in World of Warcraft

.. moduleauthor:: David Couples <gahdania@gahd.io>"""
from typing import Optional, Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class AccountAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client

    @verify_client
    def account_profile_summary(self, locale: str) -> Dict[str, Any]:
        """Accesses a summary of the account
    
        Args:
            locale (str): which locale to use for the request
    
        Returns:
            dict: JSON decoded data that contains the profile summary
        """
        data: Dict[str, Any] = self.client.protected_data(locale, 'profile')
        return data

    @verify_client
    def protected_profile_summary(self, locale: str, realm_id: int,
                                  character_id: int) -> Dict[str, Any]:
        """Accesses a summary of protected account information for the
        character identified by :realm_id: and :character_id:
    
        Args:
            locale (str): which locale to use for the request
            realm_id (int): the ID for the character's realm
            character_id (int): the ID of character
    
        Returns:
            dict: JSON decoded data that contains the protected character
                profile summary
        """
        data: Dict[str, Any] = self.client.protected_data(locale, 'profile', 'protected-character', realm_id,
                                                          character_id)
        return data

    @verify_client
    def account_collections(self, locale: str, category: Optional[str] = None) -> Dict[str, Any]:
        """Access the collection of battle pets and/or mounts of an account as
        provided by :category:
    
        Args:
            locale (str): which locale to use for the request
            category (str): 'pets' to retrieve the pet collections, and
                'mounts' to retrieve the mount collection of the account or
                None for both pets and mounts
    
        Returns:
            dict: JSON decoded data for the index/individual collections
        """
        if category is not None:
            data: Dict[str, Any] = self.client.protected_data(locale, 'profile', 'collections',
                                                              self.client.slugify(category))
        else:
            data = self.client.protected_data(locale, 'profile', 'collections')

        return data
