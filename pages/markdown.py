import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)
data_path = os.path.join(base_dir, 'datas')

def load_md(filename):
    path = os.path.join(data_path, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return f"Fichier {filename} non trouvé."

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])


block_style = {
    'backgroundColor': 'white',
    'padding': '30px',
    'border': '1px solid #333',
    'boxShadow': '10px 10px 0px #888',
    'marginBottom': '20px'
}


header_style = {
    'backgroundImage': 'url("/datas/dash.jpg")', 
    'backgroundSize': 'cover',
    'backgroundPosition': 'center',
    'padding': '60px 20px',
    'borderRadius': '5px',
    'border': '1px solid #333',
    'boxShadow': '10px 10px 0px #888',
    'marginBottom': '40px',
    'textAlign': 'center'
}

app.layout = dbc.Container(fluid=True, style={'backgroundColor': '#f4f4f4', 'minHeight': '100vh', 'padding': '40px'}, children=[
    
    html.Div(style=header_style, children=[
        html.H1("Présentation De Dash", 
                style={
                    'color': 'white', 
                    'fontWeight': 'bold', 
                    'textShadow': '2px 2px 4px #000',
                    'margin': '0'
                })
    ]),

    dbc.Row([
        dbc.Col(html.Div(style=block_style, children=[
            dbc.Accordion([
                dbc.AccordionItem(
                    dcc.Markdown(load_md('expli1.md')),
                    title="Accueil",
                ),
                dbc.AccordionItem(
                    dcc.Markdown(load_md('expli2.md')),
                    title="Layout",
                ),
                dbc.AccordionItem(
                    dcc.Markdown(load_md('expli3.md')),
                    title="CallBack",
                ),
            ], start_collapsed=True, flush=True),
        ]), width=12)
    ])
])

if __name__ == '__main__':
    app.run(debug=True)