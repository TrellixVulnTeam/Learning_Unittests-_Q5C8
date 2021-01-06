import random
from prettytable import PrettyTable

matches_table = PrettyTable()
matches_table.field_names = ['Home team', 'Away team', 'Result', 'Fans']


class Match:
    def __init__(self, home_team, away_team, fans, hts, ats):
        self.home_team = home_team
        self.away_team = away_team
        self.fans = fans
        self.hts = hts
        self.ats = ats

    def return_match_result(self):
        pass


if __name__ == '__main__':
    pass

