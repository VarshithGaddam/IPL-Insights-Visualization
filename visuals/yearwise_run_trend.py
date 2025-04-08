import plotly.express as px

def plot_yearwise_runs(df):
    fig = px.line(df, x='season', y='total_runs', markers=True,
                  title='Year-wise Total Runs in IPL')
    fig.update_layout(xaxis_title="Season", yaxis_title="Total Runs",
                      transition_duration=500)
    return fig
