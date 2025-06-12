from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import time

year = '2023'

for team in teams.get_teams():
    id = (team['id'])
    game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable= id)
    games = game_finder.get_data_frames()
    for game in games:
        print(game.head(1))

    time.sleep(0.4)