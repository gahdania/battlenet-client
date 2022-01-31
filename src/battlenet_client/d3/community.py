from src.d3_api.decorators import verify_client
from battlenet_client import slugify
from urllib.parse import quote


@verify_client
def act(client, locale, act_id=None):

    if act_id is None:
        return client.community(locale, 'act')

    return client.community(locale, 'act', act_id)


@verify_client
def artisan(client, locale, artisan_name):
    return client.community(locale, 'artisan', artisan_name)


@verify_client
def recipe(client, locale, artisan_name, recipe_slug):
    return client.community(locale, 'artisan', artisan_name, 'recipe', slugify(recipe_slug))


@verify_client
def follower(client, locale, follower_slug):
    return client.community(locale, 'follower', slugify(follower_slug))


@verify_client
def character_class(client, locale, class_slug):
    return client.community(locale, 'hero', slugify(class_slug))


@verify_client
def api_skill(client, locale, class_slug, skill_slug):
    return client.community(locale, 'hero', slugify(class_slug), 'skill', slugify(skill_slug))


@verify_client
def item_type(client, locale, item_slug=None):
    if item_slug is None:
        return client.community(locale, 'item-type')

    return client.community(locale, 'item-type', slugify(item_slug))


@verify_client
def item(client, locale, item_slug):
    return client.community(locale, 'item', item_slug)


@verify_client
def api_account(client, locale, btag):
    return client.profile_api(locale, f"{quote(btag)}/")


@verify_client
def api_hero(client, locale, btag, hero_id):
    return client.profile_api(locale, quote(btag), 'hero', hero_id)


@verify_client
def api_hero_items(client, locale, btag, hero_id):
    return client.profile_api(locale, quote(btag), 'hero', hero_id, 'items')


@verify_client
def api_follower_items(client, locale, btag, hero_id):
    return client.profile_api(locale, quote(btag), 'hero', hero_id, 'follower-items')
