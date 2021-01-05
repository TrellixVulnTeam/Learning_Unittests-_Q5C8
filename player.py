from club import Club


class Player:
    def __init__(self, first_name, last_name, team, age, position, country):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.age = age
        self.position = position
        self.country = country

    def get_player_info(self):
        return f'{self.first_name} {self.last_name} from {self.country} is playing for {self.team} at {self.position}' \
               f' position. His age - {self.age} years old'

    def transfer(self, transferred_club_name):
        if transferred_club_name in Club.clubs_registered:
            self.team = transferred_club_name
            return f'{self.first_name} {self.last_name} is transferred to {transferred_club_name}'
        else:
            raise ValueError(f'{transferred_club_name} is not in clubs_registered list')


if __name__ == '__main__':
    alexis_sanchez = Player('Alexis', 'Sanchez', 'Inter', 32, 'LW', 'Chile')
    alexis_sanchez.transfer('Arsenal')
    print(alexis_sanchez.get_player_info())
