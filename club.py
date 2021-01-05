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

