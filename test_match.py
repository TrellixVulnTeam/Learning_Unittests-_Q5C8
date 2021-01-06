import match
import unittest


class TestMatch(unittest.TestCase):
    def test_set_up_fans_less_than(self):
        self.assertEqual(match.set_up_fans(6000), 'For today\'s match will come - 6000 fans. That\'s a small number')

    def test_set_up_fans_more_than(self):
        self.assertEqual(match.set_up_fans(6500), 'For today\'s match will come - 3500 fans. That\'s a normal number')

    def test_set_up_fans_argument_type(self):
        with self.assertRaises(ValueError):
            match.set_up_fans('3444')

    def test_start_match(self):
        self.assertEqual(match.start_match('Arsenal', 'Tottenham'), 'Match between Arsenal and Tottenham starts')

    def test_start_match_argument_types(self):
        with self.assertRaises(ValueError):
            match.start_match(1213, 5123)

    def test_simulate_match(self):
        pass

    def test_append_match_result_to_table(self):
        pass
