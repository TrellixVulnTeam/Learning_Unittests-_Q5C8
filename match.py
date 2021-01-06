import club
import player
import random
from prettytable import PrettyTable


def set_up_fans(fans):
    if not isinstance(fans, int):
        raise ValueError('Fans number must be int')
    if fans >= 6250:
        return f'For today\'s match will come - {fans} fans. That\'s a normal number'
    elif fans <= 6250:
        return f'For today\'s match will come - {fans} fans. That\'s a small number'


def start_match(home_team, away_team):
    if not isinstance(home_team, str) and not isinstance(away_team, str):
        raise ValueError('Teams should be str type')
    return f'Match between {home_team} and {away_team} starts'


def simulate_match(home_scored_goals, away_scored_goals):
    if not isinstance(home_scored_goals, int) and not isinstance(away_scored_goals, int):
        raise ValueError('Goals value must be int')
    if home_scored_goals > away_scored_goals:
        return f'Home team wins. Match score {home_scored_goals}:{away_scored_goals}'
    elif home_scored_goals == away_scored_goals:
        return f'Match ended with draw result {home_scored_goals}:{away_scored_goals}'
    else:
        return f'Away team wins. Match score {home_scored_goals}:{away_scored_goals}'


def append_match_result_to_table():
    pass


if __name__ == '__main__':
    print(set_up_fans(6800))
    print(start_match('Arsenal', 'Spurs'))
    print(simulate_match(random.randint(0, 4), random.randint(0, 4)))
    print()

    print(set_up_fans(7500))
    print(start_match('Chelsea', 'Liverpool'))
    print(simulate_match(random.randint(0, 4), random.randint(0, 4)))
    print()

    print(set_up_fans(7700))
    print(start_match('Manchester United', 'Manchester City'))
    print(simulate_match(random.randint(0, 4), random.randint(0, 4)))
