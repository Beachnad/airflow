from unittest import TestCase
from datetime import date
from src.dags.scripts.sports import ncaab_boxscores


class Test(TestCase):
    def test_ncaab_boxscores(self):
        df = ncaab_boxscores(date(2020, 2, 2))
        self.assertEqual(len(df), 14, 'There should be 14 games on this date')
