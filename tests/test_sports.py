from unittest import TestCase
from scripts.sports import ncaab_boxscores
from datetime import date


class Test(TestCase):
    def test_ncaab_boxscores(self):
        df = ncaab_boxscores(date(2020, 2, 2))
        self.assertEqual(len(df), 14, 'There should be 14 games on this date')
