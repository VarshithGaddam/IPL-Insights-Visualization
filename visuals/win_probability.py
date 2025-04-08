# visuals/win_probability.py

import plotly.express as px

def plot_win_probability(df):
    fig = px.line(
        df,
        x="over",
        y="probability",  # <--- Use the correct column name
        title="Win Probability Over Overs",
        labels={"probability": "Win Probability", "over": "Over"},
        markers=True
    )
    fig.update_traces(line=dict(width=3))
    return fig
