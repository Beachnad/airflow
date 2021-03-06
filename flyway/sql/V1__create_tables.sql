CREATE SCHEMA staging;

CREATE TABLE staging.box_scores (
    box_score_id VARCHAR(128) PRIMARY KEY,
    away_assist_percentage NUMERIC,
    away_assists INT,
    away_block_percentage NUMERIC,
    away_blocks INT,
    away_defensive_rating NUMERIC,
    away_defensive_rebound_percentage NUMERIC,
    away_defensive_rebounds INT,
    away_effective_field_goal_percentage NUMERIC,
    away_field_goal_attempts INT,
    away_field_goal_percentage NUMERIC,
    away_field_goals INT,
    away_free_throw_attempt_rate NUMERIC,
    away_free_throw_attempts INT,
    away_free_throw_percentage VARCHAR(128),
    away_free_throws INT,
    away_losses INT,
    away_minutes_played INT,
    away_offensive_rating NUMERIC,
    away_offensive_rebound_percentage NUMERIC,
    away_offensive_rebounds INT,
    away_personal_fouls INT,
    away_points INT,
    away_ranking VARCHAR(128),
    away_steal_percentage NUMERIC,
    away_steals INT,
    away_three_point_attempt_rate NUMERIC,
    away_three_point_field_goal_attempts INT,
    away_three_point_field_goal_percentage NUMERIC,
    away_three_point_field_goals INT,
    away_total_rebound_percentage NUMERIC,
    away_total_rebounds INT,
    away_true_shooting_percentage NUMERIC,
    away_turnover_percentage NUMERIC,
    away_turnovers INT,
    away_two_point_field_goal_attempts INT,
    away_two_point_field_goal_percentage NUMERIC,
    away_two_point_field_goals INT,
    away_win_percentage NUMERIC,
    away_wins INT,
    date DATE,
    home_assist_percentage NUMERIC,
    home_assists INT,
    home_block_percentage NUMERIC,
    home_blocks INT,
    home_defensive_rating NUMERIC,
    home_defensive_rebound_percentage NUMERIC,
    home_defensive_rebounds INT,
    home_effective_field_goal_percentage NUMERIC,
    home_field_goal_attempts INT,
    home_field_goal_percentage NUMERIC,
    home_field_goals INT,
    home_free_throw_attempt_rate NUMERIC,
    home_free_throw_attempts INT,
    home_free_throw_percentage NUMERIC,
    home_free_throws INT,
    home_losses INT,
    home_minutes_played INT,
    home_offensive_rating NUMERIC,
    home_offensive_rebound_percentage NUMERIC,
    home_offensive_rebounds INT,
    home_personal_fouls INT,
    home_points INT,
    home_ranking VARCHAR(128),
    home_steal_percentage NUMERIC,
    home_steals INT,
    home_three_point_attempt_rate NUMERIC,
    home_three_point_field_goal_attempts INT,
    home_three_point_field_goal_percentage NUMERIC,
    home_three_point_field_goals INT,
    home_total_rebound_percentage NUMERIC,
    home_total_rebounds INT,
    home_true_shooting_percentage NUMERIC,
    home_turnover_percentage NUMERIC,
    home_turnovers INT,
    home_two_point_field_goal_attempts INT,
    home_two_point_field_goal_percentage NUMERIC,
    home_two_point_field_goals INT,
    home_win_percentage NUMERIC,
    home_wins INT,
    location VARCHAR(128),
    losing_abbr VARCHAR(128),
    losing_name VARCHAR(128),
    pace NUMERIC,
    winner VARCHAR(128),
    winning_abbr VARCHAR(128),
    winning_name VARCHAR(128)
);
