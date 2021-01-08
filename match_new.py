import random
import club
from prettytable import PrettyTable
from db_config import connection, cursor

matches_table = PrettyTable()
matches_table.field_names = ['Home team', 'Away team', 'Result', 'Fans']


def schedule():
    print(club.Club.clubs_registered)


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
    first_match = Match(club.arsenal.name, club.spurs.name, 43000, random.randint(0, 4), random.randint(0, 4))
    second_match = Match(club.arsenal.name, club.liverpool.name, 32150, random.randint(0, 4), random.randint(0, 4))
    third_match = Match(club.arsenal.name, club.man_united.name, 25025, random.randint(0, 4), random.randint(0, 4))
    fourth_match = Match(club.arsenal.name, club.man_city.name, 42100, random.randint(0, 4), random.randint(0, 4))
    fifth_match = Match(club.arsenal.name, club.chelsea.name, 31000, random.randint(0, 4), random.randint(0, 4))
    last_match = Match(club.chelsea.name, club.arsenal.name, 37000, random.randint(0, 4), random.randint(0, 4))

    matches_list = [first_match, second_match, third_match, fourth_match, fifth_match, last_match]
    for match in matches_list:
        match.return_match_result()

    print('\n', matches_table)

