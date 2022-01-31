"""Provides access to the power type API """
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class PowerAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
            
    @verify_client
    def power_type(self, locale: str, power_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of power types, or a specific power type
    
        Args:
            locale (str): which locale to use for the request
            power_id (int, optional): the power type's ID or the word 'index'
    
        Returns:
            dict: json decoded data for the index/individual power types
        """
        if power_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'power-type', power_id)
        else:
            data = self.client.game_data(locale, 'static', 'power-type', 'index')
        return data
