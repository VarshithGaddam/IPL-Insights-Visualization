
import plotly.express as px

def plot_top_batsmen(df):
    fig = px.bar(df, x='batsman', y='total_runs',
                 title='Top 10 Run Scorers in IPL',
                 color='total_runs', text='total_runs')
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title="Batsman", yaxis_title="Total Runs",
                      transition_duration=500)
    return fig
