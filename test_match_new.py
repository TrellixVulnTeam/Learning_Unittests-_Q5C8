import match_new
import unittest


class TestNewMatch(unittest.TestCase):
    def test_teams_type_int(self):
        with self.assertRaises(ValueError):
            match = match_new.Match(333, 123, 2300, 3, 1)

    def test_teams_type_none(self):
        with self.assertRaises(ValueError):
            match = match_new.Match(None, None, 2300, 3, 1)

    def test_teams_type_float(self):
        with self.assertRaises(ValueError):
            match = match_new.Match(333.4, 123.2, 2300, 3, 1)

    def test_teams_type_str(self):
        match = match_new.Match('Arsenal', 'Spurs', 2300, 3, 1)
        output = f'{match.home_team} : {match.away_team}'
        self.assertEqual(output, 'Arsenal : Spurs')

    def test_fans_type_str(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', '2300', 3, 1)

    def test_fans_type_float(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300.4, 3, 1)

    def test_fans_type_none(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', None, 3, 1)

    def test_hts_ats_type_str_both(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, '3', '1')

    def test_hts_ats_type_str_ats(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, 3, '1')

    def test_hts_ats_type_str_hts(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, '3', 1)

    def test_hts_ats_type_float_both(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, 3.2, 1.2)

    def test_hts_ats_type_float_hts(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, 3.2, 1)

    def test_hts_ats_type_float_ats(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, 3, 1.2)

    def test_hts_ats_type_none_both(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, None, None)

    def test_hts_ats_type_none_hts(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, None, 1)

    def test_hts_ats_type_none_ats(self):
        with self.assertRaises(ValueError):
            match = match_new.Match('Arsenal', 'Spurs', 2300, 3, None)

    def test_return_match_result_home_team_wins(self):
        match = match_new.Match('Arsenal', 'Spurs', 2300, 3, 1)
        actual_output = f'\n⚽ Match between {match.home_team} and {match.away_team} starts\n' \
                        f'For today\'s match will come - {match.fans} fans.' \
                        f'\n{match.home_team} {match.hts} : {match.ats} {match.away_team}'
        expected_output = f'\n⚽ Match between Arsenal and Spurs starts\n' \
                          f'For today\'s match will come - 2300 fans.' \
                          f'\nArsenal 3 : 1 Spurs'
        self.assertEqual(actual_output, expected_output)

    def test_return_match_result_away_team_wins(self):
        match = match_new.Match('Spurs', 'Arsenal', 2300, 0, 4)
        actual_output = f'\n⚽ Match between {match.home_team} and {match.away_team} starts\n' \
                        f'For today\'s match will come - {match.fans} fans.' \
                        f'\n{match.home_team} {match.hts} : {match.ats} {match.away_team}'
        expected_output = f'\n⚽ Match between Spurs and Arsenal starts\n' \
                          f'For today\'s match will come - 2300 fans.' \
                          f'\nSpurs 0 : 4 Arsenal'
        self.assertEqual(actual_output, expected_output)
