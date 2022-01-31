from sc2.decorators import verify_client


@verify_client
def league_data(client, locale, season_id, queue_id, team_type, league_id):

    return client.game_data(locale, 'league', season_id, queue_id, team_type,league_id)
