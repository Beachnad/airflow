from unittest import TestCase
from datetime import date
import pandas as pd
from src.dags.scripts.sports import ncaab_boxscores, get_adv_boxscores


class Test(TestCase):
    def test_ncaab_boxscores(self):
        data = ncaab_boxscores(date(2020, 2, 2))
        df = pd.DataFrame(data)

        self.assertEqual(len(df), 14, 'There should be 14 games on this date')
        self.assertEqual(list(df), [
            'boxscore', 'away_name', 'away_abbr', 'away_score', 'away_rank',
            'home_name', 'home_abbr', 'home_score', 'home_rank', 'non_di',
            'top_25', 'winning_name', 'winning_abbr', 'losing_name', 'losing_abbr'
        ], "Check the returned column names")

    def test_get_adv_boxscores(self):
        data = get_adv_boxscores(date(2020, 2, 2), date(2020, 2, 4))
        df = pd.DataFrame(data)

        self.assertEqual(len(df), 28, 'There should be 28 games on this date')
        self.assertEqual(list(df), [
            'away_assist_percentage', 'away_assists', 'away_block_percentage',
            'away_blocks', 'away_defensive_rating', 'away_defensive_rebound_percentage',
            'away_defensive_rebounds', 'away_effective_field_goal_percentage',
            'away_field_goal_attempts', 'away_field_goal_percentage', 'away_field_goals',
            'away_free_throw_attempt_rate', 'away_free_throw_attempts',
            'away_free_throw_percentage', 'away_free_throws', 'away_losses',
            'away_minutes_played', 'away_offensive_rating', 'away_offensive_rebound_percentage',
            'away_offensive_rebounds', 'away_personal_fouls', 'away_points', 'away_ranking',
            'away_steal_percentage', 'away_steals', 'away_three_point_attempt_rate',
            'away_three_point_field_goal_attempts', 'away_three_point_field_goal_percentage',
            'away_three_point_field_goals', 'away_total_rebound_percentage',
            'away_total_rebounds', 'away_true_shooting_percentage', 'away_turnover_percentage',
            'away_turnovers', 'away_two_point_field_goal_attempts', 'away_two_point_field_goal_percentage',
            'away_two_point_field_goals', 'away_win_percentage', 'away_wins', 'date',
            'home_assist_percentage', 'home_assists', 'home_block_percentage', 'home_blocks',
            'home_defensive_rating', 'home_defensive_rebound_percentage', 'home_defensive_rebounds',
            'home_effective_field_goal_percentage', 'home_field_goal_attempts',
            'home_field_goal_percentage', 'home_field_goals', 'home_free_throw_attempt_rate',
            'home_free_throw_attempts', 'home_free_throw_percentage', 'home_free_throws',
            'home_losses', 'home_minutes_played', 'home_offensive_rating',
            'home_offensive_rebound_percentage', 'home_offensive_rebounds', 'home_personal_fouls',
            'home_points', 'home_ranking', 'home_steal_percentage', 'home_steals',
            'home_three_point_attempt_rate', 'home_three_point_field_goal_attempts',
            'home_three_point_field_goal_percentage', 'home_three_point_field_goals',
            'home_total_rebound_percentage', 'home_total_rebounds', 'home_true_shooting_percentage',
            'home_turnover_percentage', 'home_turnovers', 'home_two_point_field_goal_attempts',
            'home_two_point_field_goal_percentage', 'home_two_point_field_goals', 'home_win_percentage',
            'home_wins', 'location', 'losing_abbr', 'losing_name', 'pace', 'winner', 'winning_abbr',
            'winning_name'
        ]
, "Check the returned column names")
