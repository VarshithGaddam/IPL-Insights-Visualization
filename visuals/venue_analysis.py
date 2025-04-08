# visuals/venue_analysis.py

import plotly.express as px

def plot_venue_analysis(df):
    fig = px.bar(
        df.sort_values("matches", ascending=False),
        x="venue",
        y="matches",
        title="Matches Played Per Venue",
        labels={"matches": "No. of Matches", "venue": "Venue"},
        color="matches"
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig
