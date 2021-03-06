from sportsreference.ncaab.boxscore import Boxscores, Boxscore
from datetime import date as Date, timedelta, datetime
import pandas as pd


def dates_between(start, end):
    if type(start) is str:
        start = datetime.strptime(start, '%Y-%m-%d')

    if type(end) is str:
        end = datetime.strptime(end, '%Y-%m-%d')

    dates = [start + timedelta(days=days) for days in range((end - start).days)]
    return dates


def season_dates(year):
    start = Date(year, 11, 1)
    end = Date(year + 1, 4, 30)

    dates = dates_between(start, end)
    return dates


def ncaab_boxscores(game_date: Date):
    date_key = f"{game_date.month}-{game_date.day}-{game_date.year}"
    return Boxscores(game_date).games[date_key]


def get_year_boxscores(start, end) -> pd.DataFrame:
    data = []
    dates = dates_between(start, end)
    for i, date in enumerate(dates, start=0):
        boxscore = ncaab_boxscores(date)
        if len(boxscore) >= 1:
            data.extend(boxscore)

    return pd.DataFrame(data)


def get_adv_boxscores(start, end):
    df = get_year_boxscores(start, end)
    if len(df) > 0:
        ids = get_year_boxscores(start, end)['boxscore'] if len(df) > 0 else pd.Series([])
        df = pd.concat([Boxscore(id).dataframe for id in ids])
        df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%B %d, %Y'))
    return df
