class Club:

    clubs_registered = []

    def __init__(self, name, year, colors):
        self.name = name
        self.year = year
        self.colors = colors
        Club.clubs_registered.append(self.name)

    def get_club_info(self):
        return f'{self.name} was found at {self.year}. They colors - {self.colors}'


arsenal = Club('Arsenal', 1886, 'Red and white')
chelsea = Club('Chelsea', 1905, 'Blue')
liverpool = Club('Liverpool', 1892, 'Red')
man_united = Club('Manchester United', 1878, 'Red')
man_city = Club('Manchester City', 1880, 'White and blue')
spurs = Club('Tottenham', 1882, 'White')

if __name__ == '__main__':
    print(', '.join(Club.clubs_registered))
