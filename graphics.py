import pygal
from matplotlib import pyplot as plt
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS
from db_config import cursor, connection


def return_all_goals_season(team):
    cursor.execute("SELECT hts FROM match_results WHERE home_team='%s';" % team)
    home_goals = cursor.fetchall()
    total_goals_scored = 0
    for hts in home_goals:
        total_goals_scored += hts[0]

    cursor.execute("SELECT ats FROM match_results WHERE away_team='%s';" % team)
    away_goals = cursor.fetchall()
    for ats in away_goals:
        total_goals_scored += ats[0]
    return total_goals_scored


print(return_all_goals_season('Arsenal'))
print(return_all_goals_season('Chelsea'))
