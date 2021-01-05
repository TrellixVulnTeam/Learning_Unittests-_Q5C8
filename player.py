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


if __name__ == '__main__':
    alexis_sanchez = Player('Alexis', 'Sanchez', 'Inter', 32, 'LW', 'Chile')
    print(alexis_sanchez.get_player_info())
