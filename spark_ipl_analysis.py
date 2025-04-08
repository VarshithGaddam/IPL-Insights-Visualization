# spark_ipl_analysis.py

from pyspark.sql import SparkSession
import random

spark = SparkSession.builder.appName("IPL Analysis").getOrCreate()

# Load data
matches = spark.read.csv("data/matches.csv", header=True, inferSchema=True)
deliveries = spark.read.csv("data/deliveries.csv", header=True, inferSchema=True)

def get_top_batsmen_df():
    return deliveries.groupBy("batsman").sum("batsman_runs") \
        .withColumnRenamed("sum(batsman_runs)", "total_runs") \
        .orderBy("total_runs", ascending=False).limit(10).toPandas()

def get_yearwise_runs_df():
    joined = deliveries.join(matches, deliveries.match_id == matches.id)
    return joined.groupBy("season").sum("total_runs") \
        .withColumnRenamed("sum(total_runs)", "total_runs") \
        .orderBy("season").toPandas()

def get_team_wins_df():
    return matches.groupBy("winner").count().orderBy("count", ascending=False).toPandas()

def get_toss_vs_win_df():
    toss_and_win = matches.filter(matches.toss_winner == matches.winner).count()
    total_matches = matches.count()
    return {"Toss & Win": toss_and_win, "Only Toss": total_matches - toss_and_win}

def get_over_heatmap_df():
    return deliveries.groupBy("match_id", "over").sum("total_runs") \
        .withColumnRenamed("sum(total_runs)", "runs").toPandas()

def get_player_season_stats():
    joined = deliveries.join(matches, deliveries.match_id == matches.id)
    return joined.groupBy("season", "batsman").sum("batsman_runs") \
        .withColumnRenamed("sum(batsman_runs)", "total_runs").toPandas()

def get_team_score_progression():
    joined = deliveries.join(matches, deliveries.match_id == matches.id)
    return joined.groupBy("season", "batting_team", "over").sum("total_runs") \
        .withColumnRenamed("sum(total_runs)", "runs").toPandas()

def get_batsman_stats(player_name):
    return deliveries.filter(deliveries.batsman == player_name) \
        .groupBy("match_id").sum("batsman_runs") \
        .withColumnRenamed("sum(batsman_runs)", "runs").toPandas()

def get_unique_years():
    return [row["season"] for row in matches.select("season").distinct().collect()]

def get_unique_teams():
    return [row["batting_team"] for row in deliveries.select("batting_team").distinct().collect()]

def get_unique_venues():
    return [row["venue"] for row in matches.select("venue").distinct().collect()]

def get_leaderboard():
    return deliveries.groupBy("batsman") \
        .agg({"batsman_runs": "sum", "match_id": "count"}) \
        .withColumnRenamed("sum(batsman_runs)", "total_runs") \
        .withColumnRenamed("count(match_id)", "matches") \
        .orderBy("total_runs", ascending=False).toPandas().head(20)

def predict_match_outcome(team1, team2):
    wins = matches.filter((matches["winner"] == team1) | (matches["winner"] == team2))
    win_counts = wins.groupBy("winner").count().toPandas().set_index("winner").to_dict()["count"]
    return max(win_counts, key=win_counts.get) if win_counts else random.choice([team1, team2])

def get_win_probability_data():
    import numpy as np
    joined = deliveries.join(matches, deliveries.match_id == matches.id)
    df = joined.groupBy("match_id", "season", "batting_team", "over").sum("total_runs") \
        .withColumnRenamed("sum(total_runs)", "runs").toPandas()
    df["cumulative_runs"] = df.groupby(["match_id", "batting_team"])["runs"].cumsum()
    df["max_runs"] = df.groupby("match_id")["cumulative_runs"].transform("max")
    df["win_prob"] = df["cumulative_runs"] / df["max_runs"]
    df["win_prob"] = df["win_prob"].fillna(0)
    return df

def get_venue_analysis_df():
    return matches.groupBy("venue").count() \
        .withColumnRenamed("count", "matches").orderBy("matches", ascending=False).toPandas()

# Placeholder functions
def calculate_win_probability(team1, team2, score, overs, wickets):
    import random
    return [{"over": i, "probability": min(1.0, max(0.0, (score + i * 6 - wickets * 5) / 300))} for i in range(1, 21)]

def get_live_scoreboard_data():
    import pandas as pd
    import numpy as np
    return pd.DataFrame({
        "Over": np.arange(1, 21),
        "Team A Score": np.random.randint(2, 12, 20).cumsum(),
        "Team B Score": np.random.randint(2, 12, 20).cumsum()
    })
