import plotly.express as px
import plotly.offline as pyo


def get_graph_animation():
    df = px.data.gapminder()
    fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
               size="pop", color="continent", hover_name="country",
               log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90],
                     )
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='lightgray'),
                        autosize=True,
                        margin=dict(l=25, r=35, t=10, b=0),
                        )
    fig_div = pyo.plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)
    return fig_div


def get_bar_plot_animation():
    df = px.data.gapminder()
    fig = px.bar(df, x="continent", y="pop", color="continent",
                 animation_frame="year", range_y=[0, 4000000000])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='lightgray'),
                        autosize=True,
                        margin=dict(l=25, r=35, t=10, b=0),
                        )
    fig_div = pyo.plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)
    return fig_div