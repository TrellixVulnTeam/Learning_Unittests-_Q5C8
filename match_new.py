import random
from prettytable import PrettyTable
from db_config import connection, cursor

matches_table = PrettyTable()
matches_table.field_names = ['Home team', 'Away team', 'Result', 'Fans']


class Match:
    def __init__(self, home_team, away_team, fans, hts, ats):
        self.home_team = home_team
        self.away_team = away_team
        self.fans = fans
        self.hts = hts
        self.ats = ats

    def insert_match_result(self):
        insert_match_result_query = f"INSERT INTO match_results(home_team, away_team, fans, hts, ats)" \
                                    f"VALUES('%s', '%s', %s, %s, %s);" % \
                                    (self.home_team, self.away_team, self.fans, self.hts, self.ats)
        cursor.execute(insert_match_result_query)
        connection.commit()

    def return_match_result(self):
        if not isinstance(self.home_team, str) and not isinstance(self.away_team, str):
            raise ValueError('Home team and Away team should be str type')
        if not isinstance(self.fans, int) and not isinstance(self.hts, int) and not isinstance(self.ats, int):
            raise ValueError('Arguments fans, hts, ats should be int type')
        match_result = f'\n⚽ Match between {self.home_team} and {self.away_team} starts\n' \
                       f'For today\'s match will come - {self.fans} fans.' \
                       f'\n{self.home_team} {self.hts} : {self.ats} {self.away_team}'
        matches_table.add_row([self.home_team, self.away_team, f'{self.hts} : {self.ats}', self.fans])
        self.insert_match_result()
        return match_result


if __name__ == '__main__':
    first_match = Match('Arsenal', 'Liverpool', 23000, random.randint(0, 4), random.randint(0, 4))
    second_match = Match('Chelsea', 'Manchester United', 31000, random.randint(0, 4), random.randint(0, 4))
    third_match = Match('Manchester City', 'Tottenham', 27000, random.randint(0, 4), random.randint(0, 4))
    first_match.return_match_result()
    second_match.return_match_result()
    third_match.return_match_result()
    first_match.insert_match_result()
    print('\n', matches_table)

