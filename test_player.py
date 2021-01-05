import unittest
from player import Player


class MethodsTestCase(unittest.TestCase):
    def test_get_player_info(self):
        player_obj = Player('Alexis', 'Sanchez', 'Inter', 32, 'LW', 'Chile')
        output = player_obj.get_player_info()
        self.assertEqual(output,
                         'Alexis Sanchez from Chile is playing for Inter at LW position. His age - 32 years old')

    def test_player_object_data_types(self):
        player_obj = Player('Lukas', 'Podolski', 'Antalyaspor', 35, 'ST', 'Germany')
        self.assertIsInstance(player_obj.first_name, str)
        self.assertIsInstance(player_obj.last_name, str)
        self.assertIsInstance(player_obj.team, str)
        self.assertIsInstance(player_obj.age, int)
        self.assertIsInstance(player_obj.position, str)
        self.assertIsInstance(player_obj.country, str)

    def test_transfer(self):
        alexandre_lacazette = Player('Alexandre', 'Lacazette', 'Arsenal', 29, 'ST', 'France')
        alexandre_lacazette.transfer('PSG')
        self.assertEqual(alexandre_lacazette.team, 'PSG')
        self.assertIsInstance(alexandre_lacazette.team, str)

