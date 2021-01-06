import match
import unittest


class TestMatch(unittest.TestCase):
    def test_set_up_fans_less_than(self):
        self.assertEqual(match.set_up_fans(6000), 'For today\'s match will come - 6000 fans. That\'s a small number')

    def test_set_up_fans_more_than(self):
        self.assertEqual(match.set_up_fans(6500), 'For today\'s match will come - 6500 fans. That\'s a normal number')

    def test_set_up_fans_argument_type(self):
        with self.assertRaises(ValueError):
            match.set_up_fans('3444')

    def test_start_match(self):
        self.assertEqual(match.start_match('Arsenal', 'Tottenham'), 'Match between Arsenal and Tottenham starts')

    def test_start_match_argument_types_int(self):
        with self.assertRaises(ValueError):
            match.start_match(1213, 5123)

    def test_start_match_argument_float(self):
        with self.assertRaises(ValueError):
            match.start_match(1213.4, 5123.2)

    def test_simulate_match_home_team_wins(self):
        self.assertEqual(match.simulate_match(3, 2), 'Home team wins. Match score 3:2')

    def test_simulate_match_away_team_wins(self):
        self.assertEqual(match.simulate_match(2, 3), 'Away team wins. Match score 2:3')

    def test_simulate_match_draw(self):
        self.assertEqual(match.simulate_match(1, 1), 'Match ended with draw result 1:1')

    def test_simulate_match_argument_type_str(self):
        with self.assertRaises(ValueError):
            match.simulate_match('2', '3')

    def test_simulate_match_argument_type_float(self):
        with self.assertRaises(ValueError):
            match.simulate_match(2.5, 3.7)

    def test_simulate_match_argument_type_boolean(self):
        with self.assertRaises(ValueError):
            match.simulate_match(True, False)

    def test_simulate_match_argument_types(self):
        with self.assertRaises(ValueError):
            match.simulate_match('2', '3')

    def test_append_match_result_to_table(self):
        pass
