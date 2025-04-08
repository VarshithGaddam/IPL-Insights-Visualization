import plotly.express as px

def plot_team_wins(df):
    fig = px.pie(df, values='count', names='winner',
                 title='Match Wins by Team', hole=0.4)
    fig.update_traces(textinfo='percent+label')
    return fig
