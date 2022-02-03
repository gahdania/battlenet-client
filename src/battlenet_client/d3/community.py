from typing import Optional, Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from client import D3Client

from urllib.parse import quote


class CommunityAPI:
    def __init__(self, client: "D3Client") -> None:
        self.client = client

    def act(self, locale: str, act_id: Optional[int] = None) -> Dict[str, Any]:

        if act_id:
            return self.client.community(locale, "act", act_id)

        return self.client.community(locale, "act")

    def artisan(self, locale: str, artisan_name: str) -> Dict[str, Any]:
        return self.client.community(locale, "artisan", artisan_name)

    def recipe(
        self, locale: str, artisan_name: str, recipe_slug: str
    ) -> Dict[str, Any]:
        return self.client.community(
            locale, "artisan", artisan_name, "recipe", self.client.slugify(recipe_slug)
        )

    def follower(self, locale: str, follower_slug: str) -> Dict[str, Any]:
        return self.client.community(
            locale, "follower", self.client.slugify(follower_slug)
        )

    def character_class(self, locale: str, class_slug: str) -> Dict[str, Any]:
        return self.client.community(locale, "hero", self.client.slugify(class_slug))

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

    def item_type(self, locale: str, item_slug: Optional[str] = None) -> Dict[str, Any]:
        if item_slug:
            return self.client.community(
                locale, "item-type", self.client.slugify(item_slug)
            )

        return self.client.community(locale, "item-type")

    def item(self, locale: str, item_slug: str) -> Dict[str, Any]:
        return self.client.community(locale, "item", item_slug)

    def api_account(self, locale: str, b_tag: str) -> Dict[str, Any]:
        return self.client.profile_api(locale, f"{quote(b_tag)}/")

    def api_hero(
        self, locale: str, b_tag: str, hero_id: str, category: Optional[str] = None
    ) -> Dict[str, Any]:
        if category:
            if category in ("items", "follower-items"):
                return self.client.profile_api(
                    locale, quote(b_tag), "hero", hero_id, category
                )
            else:
                raise ValueError(
                    "Invalid category;  Valid catgories are 'items' and 'follower-items'"
                )
        else:
            return self.client.profile_api(locale, quote(b_tag), "hero", hero_id)