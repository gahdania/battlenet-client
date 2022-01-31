from src.d3_api.decorators import verify_client


@verify_client
def season(client, locale, season_id=None):
    if season_id is None:
        return client.game_data(locale, 'season/')

    return client.game_data(locale, 'season', season_id)


@verify_client
def season_leaderboard(client, locale, season_id, leaderboard_id):
    return client.game_data(locale, 'season', season_id, 'leaderboard', leaderboard_id)


@verify_client
def era(client, locale, era_id=None):

    if era_id is None:
        return client.game_data(locale, 'era/')
    
    return client.game_data(locale, 'era', era_id)


@verify_client
def era_leaderboard(client, locale, era_id, leaderboard_id):
    return client.game_data(locale, 'era', era_id, 'leaderboard', leaderboard_id)
