class Club:
    def __init__(self, name, year, colors):
        self.name = name
        self.year = year
        self.colors = colors

    def get_club_info(self):
        return f'{self.name} was found at {self.year}. They colors - {self.colors}'


if __name__ == '__main__':
    arsenal = Club('Arsenal', 1886, 'Red and white')
    print(arsenal.get_club_info())
