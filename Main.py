from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

for team in teams.get_teams():
    id = (team['id'])
    game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable= id)
    