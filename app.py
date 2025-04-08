# app.py

import streamlit as st
import pandas as pd
from spark_ipl_analysis import *

from visuals.top_batsmen_plot import plot_top_batsmen
from visuals.yearwise_run_trend import plot_yearwise_runs
from visuals.match_wins_plot import plot_team_wins
from visuals.toss_vs_win import plot_toss_vs_win
from visuals.runs_per_over_heatmap import plot_over_heatmap
from visuals.animated_player_trend import plot_player_season_animation
from visuals.team_score_progression import plot_team_score_progression
from visuals.venue_analysis import plot_venue_analysis
from visuals.win_probability import plot_win_probability
from visuals.scoreboard import plot_scoreboard
import plotly.express as px

st.set_page_config(layout="wide", page_title="IPL Analytics Dashboard")

theme = st.sidebar.radio("Select Theme", ["Light", "Dark"])
custom_css = {
    "Light": """<style>body { background: white; color: black; }</style>""",
    "Dark": """<style>body { background: #0e1117; color: white; } .stApp { background: #0e1117; }</style>"""
}
st.markdown(custom_css[theme], unsafe_allow_html=True)

teams = get_unique_teams()
years = get_unique_years()
venues = get_unique_venues()

selected_team = st.sidebar.selectbox("Select Team", ["All"] + sorted(teams))
selected_year = st.sidebar.selectbox("Select Year", ["All"] + sorted(years))
selected_venue = st.sidebar.selectbox("Select Venue", ["All"] + sorted(venues))

st.title("🏏 IPL Analytics Dashboard")

with st.expander("Top 10 Batsmen"):
    df = get_top_batsmen_df()
    st.plotly_chart(plot_top_batsmen(df), use_container_width=True)

with st.expander("Year-wise Runs Trend"):
    df = get_yearwise_runs_df()
    st.plotly_chart(plot_yearwise_runs(df), use_container_width=True)

with st.expander("Match Wins by Team"):
    df = get_team_wins_df()
    st.plotly_chart(plot_team_wins(df), use_container_width=True)

with st.expander("Toss vs Match Win Impact"):
    data = get_toss_vs_win_df()
    st.plotly_chart(plot_toss_vs_win(data), use_container_width=True)

with st.expander("Runs per Over Heatmap"):
    df = get_over_heatmap_df()
    plot_over_heatmap(df)
    st.image("over_heatmap.png")

with st.expander("Animated Player Trends"):
    df = get_player_season_stats()
    st.plotly_chart(plot_player_season_animation(df), use_container_width=True)

with st.expander("Team Score Progression (Animated)"):
    df = get_team_score_progression()
    if selected_team != "All":
        df = df[df["batting_team"] == selected_team]
    if selected_year != "All":
        df = df[df["season"] == selected_year]
    st.plotly_chart(plot_team_score_progression(df), use_container_width=True)

with st.expander("📍 Venue-based Match Statistics"):
    df = get_venue_analysis_df()
    if selected_venue != "All":
        df = df[df["venue"] == selected_venue]
    st.plotly_chart(plot_venue_analysis(df), use_container_width=True)

with st.expander("Compare Players"):
    player1 = st.text_input("Enter Player 1 Name")
    player2 = st.text_input("Enter Player 2 Name")
    if player1 and player2:
        df1 = get_batsman_stats(player1)
        df2 = get_batsman_stats(player2)
        df1["Player"] = player1
        df2["Player"] = player2
        df = pd.concat([df1, df2])
        fig = px.box(df, x="Player", y="runs", title="Player Performance Comparison")
        st.plotly_chart(fig, use_container_width=True)

with st.expander("🏆 Leaderboard (Top Players)"):
    df = get_leaderboard()
    st.dataframe(df)

with st.expander("🤖 Predict Match Winner"):
    team1 = st.selectbox("Select Team 1", sorted(teams), key="p1")
    team2 = st.selectbox("Select Team 2", sorted(teams), key="p2")
    if st.button("Predict Winner"):
        pred = predict_match_outcome(team1, team2)
        st.success(f"🏆 Predicted Winner: **{pred}**")

with st.expander("📊 Win Probability Predictor"):
    team1 = st.selectbox("Batting Team", sorted(teams), key="prob1")
    team2 = st.selectbox("Bowling Team", sorted(teams), key="prob2")
    score = st.slider("Current Score", 0, 300, 100)
    overs = st.slider("Overs Completed", 0.0, 20.0, 10.0, step=0.1)
    wickets = st.slider("Wickets Lost", 0, 10, 3)
    if st.button("Calculate Win Probability"):
        prob_data = calculate_win_probability(team1, team2, score, overs, wickets)
        st.plotly_chart(plot_win_probability(prob_data), use_container_width=True)

with st.expander("📟 Dynamic Scoreboard Visualizer"):
    df = get_live_scoreboard_data()
    st.plotly_chart(plot_scoreboard(df), use_container_width=True)

st.markdown("""---\n<center>Gaddam Varshith 🚀 | Made with ❤️ using Spark, Pandas, and Streamlit</center>""", unsafe_allow_html=True)
