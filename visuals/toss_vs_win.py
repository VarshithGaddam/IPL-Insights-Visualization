import plotly.express as px

def plot_toss_vs_win(data):
    labels = list(data.keys())
    values = list(data.values())
    fig = px.pie(values=values, names=labels,
                 title="Toss vs Match Win Impact")
    return fig
