import plotly.express as px

def plot_player_season_animation(df):
    top_players = df.groupby("batsman")['total_runs'].sum().nlargest(5).index
    df = df[df['batsman'].isin(top_players)]
    fig = px.bar(df, x="batsman", y="total_runs", color="batsman",
                 animation_frame="season", range_y=[0, df.total_runs.max() + 100],
                 title="Top 5 Batsmen Over Seasons")
    return fig