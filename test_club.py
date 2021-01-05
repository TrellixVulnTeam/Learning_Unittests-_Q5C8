import unittest
from club import Club


class MethodsTestCase(unittest.TestCase):
    # def test_get_club_info(self):
    #     arsenal_obj = Club('Arsenal', 1886, 'Red and white')
    #     output = arsenal_obj.get_club_info()
    #     self.assertEqual(output, 'Arsenal was found at 1886. They colors - Red and white')
    #     self.assertEqual(arsenal_obj.name, 'Arsenal')
    #
    # def test_object_data_types(self):
    #     chelsea_obj = Club('Chelsea', 1905, 'Blue')
    #     self.assertIsInstance(chelsea_obj.name, str)
    #     self.assertIsInstance(chelsea_obj.year, int)
    #     self.assertIsInstance(chelsea_obj.colors, str)
    #
    # def test_one_club_in_registered_list(self):
    #     club_obj = Club('Chelsea', 1905, 'Blue')
    #     club_registered_list = Club.clubs_registered
    #     self.assertIsInstance(club_registered_list, list)
    #     self.assertEqual(''.join(club_registered_list), 'Chelsea')

    def test_some_clubs_in_registered_list(self):
        club_registered_list = Club.clubs_registered
        self.assertEqual(', '.join(club_registered_list), 'Arsenal, Chelsea, Liverpool, Manchester United,'
                                                          ' Manchester City, Tottenham')
