import unittest
from club import Club


class MethodsTestCase(unittest.TestCase):
    def test_get_club_info(self):
        club_obj = Club('Arsenal', 1886, 'Red and white')
        output = club_obj.get_club_info()
        self.assertEqual(output, 'Arsenal was found at 1886. They colors - Red and white')
        self.assertEqual(club_obj.name, 'Arsenal')

    def test_object_data_types(self):
        club_obj = Club('Chelsea', 1905, 'Blue')
        self.assertIsInstance(club_obj.name, str)
        self.assertIsInstance(club_obj.year, int)
        self.assertIsInstance(club_obj.colors, str)

