from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


df = pd.read_csv("daily_sales_data_pink_morsels.csv")
# sort by date
df = df.sort_values(by="date")

app = Dash(__name__)

app.layout = html.Div([
    html.H2(children="Daily Sales of Pink Morsels", style={"textAlign": "center"}),
    dcc.Graph(figure=px.line(df, x="date", y="sales", title="Pink Morsel Sales")),

])

if __name__ == '__main__':
    app.run(debug=True)
