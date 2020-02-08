from unittest import TestCase
from datetime import date, datetime
import pandas as pd
from src.dags.scripts.sports import ncaab_boxscores, dates_between


def test_ncaab_boxscores():
    data = ncaab_boxscores(date(2020, 2, 2))
    df = pd.DataFrame(data)

    assert len(df) == 14, "Test failed, data frame should have had 14 rows."
    assert list(df) == [
            'boxscore', 'away_name', 'away_abbr', 'away_score', 'away_rank',
            'home_name', 'home_abbr', 'home_score', 'home_rank', 'non_di',
            'top_25', 'winning_name', 'winning_abbr', 'losing_name', 'losing_abbr'
        ], "Test failed, check the column names of the data frame."


def test_dates_between():
    dates = dates_between("2020-01-01", "2020-01-07")
    assert dates == [datetime(2020, 1, 1, 0, 0), datetime(2020, 1, 2, 0, 0),
                     datetime(2020, 1, 3, 0, 0), datetime(2020, 1, 4, 0, 0),
                     datetime(2020, 1, 5, 0, 0), datetime(2020, 1, 6, 0, 0)], "Test failed"
