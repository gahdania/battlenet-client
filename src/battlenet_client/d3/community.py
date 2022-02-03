from typing import Optional, Any, TYPE_CHECKING, Dict, Union

if TYPE_CHECKING:
    from client import D3Client

from decorators import verify_client
from urllib.parse import quote


class CommunityAPI:
    def __init__(self, client: "D3Client") -> None:
        self.client = client

    @verify_client
    def act(
        self, locale: str, act_id: Optional[Union[str, int]] = None
    ) -> Dict[str, Any]:

        if act_id:
            return self.client.community(locale, "act", act_id)

        return self.client.community(locale, "act")

    @verify_client
    def artisan(self, locale: str, artisan_name: str) -> Dict[str, Any]:
        return self.client.community(locale, "artisan", artisan_name)

    @verify_client
    def recipe(
        self, locale: str, artisan_name: str, recipe_slug: str
    ) -> Dict[str, Any]:
        return self.client.community(
            locale, "artisan", artisan_name, "recipe", self.client.slugify(recipe_slug)
        )

    @verify_client
    def follower(self, locale: str, follower_slug: str) -> Dict[str, Any]:
        return self.client.community(
            locale, "follower", self.client.slugify(follower_slug)
        )

    @verify_client
    def character_class(self, locale: str, class_slug: str) -> Dict[str, Any]:
        return self.client.community(locale, "hero", self.client.slugify(class_slug))

    @verify_client
    def api_skill(
        self, locale: str, class_slug: str, skill_slug: str
    ) -> Dict[str, Any]:
        return self.client.community(
            locale,
            "hero",
            self.client.slugify(class_slug),
            "skill",
            self.client.slugify(skill_slug),
        )

    @verify_client
    def item_type(self, locale: str, item_slug: Optional[str] = None) -> Dict[str, Any]:
        if item_slug:
            return self.client.community(
                locale, "item-type", self.client.slugify(item_slug)
            )

        return self.client.community(locale, "item-type")

    @verify_client
    def item(self, locale: str, item_slug: str) -> Dict[str, Any]:
        return self.client.community(locale, "item", item_slug)

    @verify_client
    def api_account(self, locale: str, b_tag: str) -> Dict[str, Any]:
        return self.client.profile_api(locale, f"{quote(b_tag)}/")

    @verify_client
    def api_hero(self, locale: str, b_tag: str, hero_id: str) -> Dict[str, Any]:
        return self.client.profile_api(locale, quote(b_tag), "hero", hero_id)

    @verify_client
    def api_hero_items(self, locale: str, b_tag: str, hero_id: str) -> Dict[str, Any]:
        return self.client.profile_api(locale, quote(b_tag), "hero", hero_id, "items")

    @verify_client
    def api_follower_items(
        self, locale: str, b_tag: str, hero_id: str
    ) -> Dict[str, Any]:
        return self.client.profile_api(
            locale, quote(b_tag), "hero", hero_id, "follower-items"
        )
