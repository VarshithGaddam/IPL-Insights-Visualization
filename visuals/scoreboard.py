# visuals/scoreboard.py

import plotly.graph_objects as go

def plot_scoreboard(df):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["Over"], y=df["Team A Score"],
        mode='lines+markers',
        name='Team A',
        line=dict(color='blue')
    ))
    
    fig.add_trace(go.Scatter(
        x=df["Over"], y=df["Team B Score"],
        mode='lines+markers',
        name='Team B',
        line=dict(color='red')
    ))
    
    fig.update_layout(
        title="Live Score Progression",
        xaxis_title="Over",
        yaxis_title="Score",
        legend_title="Teams",
        template="plotly_dark"
    )
    
    return fig
