import pandas as pd
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir) 
file_path = os.path.join(base_dir, 'datas', 'avocado.csv')

df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by="Date")

y_min = df['AveragePrice'].min()
y_max = df['AveragePrice'].max()

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

block_style = {
    'backgroundColor': 'white',
    'padding': '20px',
    'border': '1px solid #333',
    'boxShadow': '10px 10px 0px #888',
    'marginBottom': '20px'
}

app.layout = dbc.Container(fluid=True, style={'backgroundColor': '#f4f4f4', 'minHeight': '100vh', 'padding': '30px'}, children=[
    
    html.H1("Prix Moyen dans le temps", 
            style={'color': '#007bff', 'textAlign': 'center', 'fontWeight': 'bold', 'marginBottom': '40px'}),

    dbc.Row([
        dbc.Col(html.Div(style=block_style, children=[
            html.Label("Région1 :", className="fw-bold mb-2"),
            dcc.Dropdown(
                id='region-1-dropdown',
                options=[{'label': r, 'value': r} for r in sorted(df['region'].unique())],
                value='Albany',
                clearable=False
            )
        ]), xs=12, md=6),
        
        dbc.Col(html.Div(style=block_style, children=[
            html.Label("Région2 :", className="fw-bold mb-2"),
            dcc.Dropdown(
                id='region-2-dropdown',
                options=[{'label': r, 'value': r} for r in sorted(df['region'].unique())],
                value='TotalUS',
                clearable=False
            )
        ]), xs=12, md=6),
    ]),

    dbc.Row([
        dbc.Col(html.Div(style=block_style, children=[
            dcc.Graph(id='graph-region-1')
        ]), xs=12, md=6),
        
        dbc.Col(html.Div(style=block_style, children=[
            dcc.Graph(id='graph-region-2')
        ]), xs=12, md=6),
    ])
])

@app.callback(
    Output('graph-region-1', 'figure'),
    Input('region-1-dropdown', 'value')
)
def update_graph1(region_name):
    dff = df[df['region'] == region_name]
    fig = px.line(dff, x='Date', y='AveragePrice', 
                  title=f"Evolution du prix moyen à {region_name}")
    fig.update_yaxes(range=[y_min, y_max])
    fig.update_traces(line_color='#007bff')
    fig.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=50, b=20))
    return fig

@app.callback(
    Output('graph-region-2', 'figure'),
    Input('region-2-dropdown', 'value')
)
def update_graph2(region_name):
    dff = df[df['region'] == region_name]
    fig = px.line(dff, x='Date', y='AveragePrice', 
                  title=f"Evolution du prix moyen à {region_name}")
    fig.update_yaxes(range=[y_min, y_max])
    fig.update_traces(line_color='#007bff')
    fig.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=50, b=20))
    return fig

if __name__ == '__main__':
    app.run(debug=True)