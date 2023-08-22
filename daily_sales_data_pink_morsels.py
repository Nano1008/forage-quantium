from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px


df = pd.read_csv("daily_sales_data_pink_morsels.csv")
# sort by date
df = df.sort_values(by="date")

app = Dash(__name__)

app.layout = html.Div([
    html.H2(children="Daily Sales of Pink Morsels", id="app-header"),
    dcc.Graph(id="graph"),
    dcc.RadioItems(id="radioitems", options=["north", "east", "south", "west", "all"], value="all", inline=True)

])


@app.callback(
    Output(component_id="graph", component_property="figure"),
    Input(component_id="radioitems", component_property="value")
)

def update_line_chart(region):
    if region == "north" or region == "east" or region == "south" or region == "west":
        filter_df = df[df["region"] == region]
    else:
        filter_df = df

    figure = px.line(filter_df, x="date", y="sales", title="Pink Morsel Sales")

    return figure


if __name__ == '__main__':
    app.run(debug=True)
