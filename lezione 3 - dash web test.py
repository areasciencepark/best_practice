import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go

import dash
from dash import Dash, dcc, html, Input, Output


df = pd.read_excel("Trieste_tas_rcp4.5.xlsx")
del df["Unnamed: 0"]
df = pd.DataFrame(df)
df['year'] = pd.DatetimeIndex(df['Date']).year
df = df.groupby("year").mean()
df = pd.DataFrame(df).reset_index()
fig = px.line(df, x="year", y="5")
fig.show()


#app = dash.Dash(__name__)
#app.layout = html.Div([
#
#    html.H1("Temperatura media per comune in FVG", style={'text-align': 'center'}),
#
#    dcc.Dropdown(id="slct_year",
#                 options=[
#                     {"label": "2015", "value": 2015},
#                     {"label": "2016", "value": 2016},
#                     {"label": "2017", "value": 2017},
#                     {"label": "2018", "value": 2018}],
#                 multi=False,
#                 value=2015,
#                 style={'width': "40%"}
#                 ),
#
#    html.Div(id='output_container', children=[]),
#    html.Br(),
#
#    dcc.Graph(id='my_bee_map', figure={})
#
#])