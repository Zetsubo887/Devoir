import pandas as pd
from dash import Dash, html, dcc, dash_table, Input, Output
import dash_bootstrap_components as dbc
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir) 
file_path = os.path.join(base_dir, 'datas', 'avocado.csv')

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Erreur : fichier non trouvé à l'emplacement {file_path}")
    df = pd.DataFrame()


cols_to_exclude = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
df_display = df.drop(columns=[c for c in cols_to_exclude if c in df.columns])


app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])


block_style = {
    'backgroundColor': 'white',
    'padding': '20px',
    'border': '1px solid #333',
    'boxShadow': '10px 10px 0px #888',
    'marginBottom': '25px'
}


app.layout = dbc.Container(fluid=True, style={'backgroundColor': '#f4f4f4', 'minHeight': '100vh', 'padding': '40px'}, children=[
    
    
    dbc.Row([
        
        dbc.Col(html.Div(style=block_style, children=[
            html.Label("Sélectionner la région :", className="fw-bold mb-2"),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': r, 'value': r} for r in sorted(df['region'].unique())],
                value='Albany',
                clearable=False
            )
        ]), xs=12, md=6),


        dbc.Col(html.Div(style=block_style, children=[
            html.Label("Sélectionner le type :", className="fw-bold mb-2"),
            dcc.Dropdown(
                id='type-dropdown',
                options=[{'label': t, 'value': t} for t in sorted(df['type'].unique())] + [{'label': 'Tous', 'value': 'Tous'}],
                value='Tous',
                clearable=False
            )
        ]), xs=12, md=6),
    ]),

    
    dbc.Row([
        dbc.Col(html.Div(style=block_style, children=[
            dash_table.DataTable(
                id='avocado-table',
                columns=[{"name": i, "id": i} for i in df_display.columns],
                data=df_display.to_dict('records'),
                page_size=10,
                style_header={
                    'backgroundColor': '#1E90FF',
                    'color': 'white',
                    'fontWeight': 'bold',
                    'border': '1px solid #333'
                },
                style_cell={'textAlign': 'left', 'padding': '10px'},
                style_data_conditional=[
                    {'if': {'row_index': 'odd'}, 'backgroundColor': '#f9f9f9'}
                ],
                style_table={'overflowX': 'auto'}
            )
        ]), width=12)
    ])
])

@app.callback(
    Output('avocado-table', 'data'),
    Input('region-dropdown', 'value'),
    Input('type-dropdown', 'value')
)
def update_table(region_val, type_val):
    dff = df_display[df_display['region'] == region_val]
    if type_val != 'Tous':
        dff = dff[dff['type'] == type_val]
    return dff.to_dict('records')

if __name__ == '__main__':
    app.run(debug=True)