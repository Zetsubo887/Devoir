import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__, 
    use_pages=True,       
    external_stylesheets=[dbc.themes.FLATLY]
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Données", href="/pages1")),
        dbc.NavItem(dbc.NavLink("Comparaison", href="/pages2")),
        dbc.NavItem(dbc.NavLink("Présentation", href="/markdown")),
    ],
    brand="Avocado Analytics",
    color="primary",
    dark=True,
    className="mb-4"
)

app.layout = html.Div([
    navbar,
    dbc.Container(dash.page_container, fluid=True)
])

if __name__ == '__main__':
    app.run(debug=True)