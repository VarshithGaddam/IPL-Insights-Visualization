import plotly.express as px

def plot_team_score_progression(df):
    fig = px.line(df, x="over", y="runs", color="batting_team",
                  animation_frame="season",
                  title="Team Score Progression by Over (Animated)")
    return fig