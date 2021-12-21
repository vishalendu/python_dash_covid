import pandas as pd

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input,Output

import plotly
import plotly.express as px

### Load Data
df = pd.read_excel('COVID-19-geographic-disbtribution-worldwide-2020-03-29.xlsx')
dff = df.groupby('countriesAndTerritories',as_index=False)[['deaths','cases']].sum()

### Functions Used for plotting
def getPie(df,col):
    return px.pie(data_frame=df,names='countriesAndTerritories',
                  values=col,hole=.3,labels={'countriesAndTerritories':'Countries'})


def getLine(df,col):
    return px.line(data_frame=df,x='dateRep',
                   y=col,color='countriesAndTerritories',
                  labels={'countriesAndTerritories':'Countries','dateRep':'Date'})

### Main code for Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

app.layout = dbc.Container([
                  dbc.Row([
                       dbc.Col(html.H1("Covid Data And Associated Graphs"
                               ,className="text-center text-primary,mb-1")
                               ,width=12)
                  ]),
                  dbc.Row([
                      dbc.Col([dash_table.DataTable(id='datatable1',
                                           columns = [
                                                     {"name":i,"id":i,"deletable":False,
                                                      "selectable":False} for i in dff.columns],
                                           page_size=6,
                                           editable=False,
                                           sort_mode="multi",
                                           row_selectable="multi",
                                           filter_action="native",
                                           sort_action="native",
                                           selected_rows=[],
                                           page_action="native",
                                           page_current=0,
                                           style_cell={"textAlign":"left"},
                                           style_cell_conditional=[
                                            {'if':{'column_id':'countriesAndTerritories'},
                                              "width":"70px"},
                                            {'if':{'column_id':'deaths'},
                                              "width":"30px"},
                                            {'if':{'column_id':'cases'},
                                              "width":"30px"}],
                                           #fill_width=False,
                                           data=dff.to_dict('records'))

                                ],xs=12, sm=12, md=12, lg=2, xl=2)
                         ]),
                   dbc.Row([
                       dbc.Col([
                           dcc.Dropdown(id="dpdwn1",
                                        options=[
                                            {"label":"Deaths","value":"deaths"},
                                            {"label":"Cases","value":"cases"}
                                        ],
                                        value="deaths",
                                        multi=False,
                                        clearable=False
                                       )
                       ],xs=12, sm=12, md=12, lg=6, xl=6),
                       dbc.Col([
                           dcc.Dropdown(id="dpdwn2",
                                        options=[
                                            {"label":"Deaths","value":"deaths"},
                                            {"label":"Cases","value":"cases"}
                                        ],
                                        value="cases",
                                        multi=False,
                                        clearable=False
                                       )
                       ],xs=12, sm=12, md=12, lg=6, xl=6)
                   ]),
                 dbc.Row([
                     dbc.Col([
                         dcc.Graph(id="lineplot")
                     ],xs=12, sm=12, md=12, lg=6, xl=6),
                     dbc.Col([
                         dcc.Graph(id="piechart")
                     ],xs=12, sm=12, md=12, lg=6, xl=6)
                 ])
], fluid=True)


#### implement callback
@app.callback(
    [Output('lineplot', 'figure'),
     Output('piechart', 'figure')],
    [Input('datatable1', 'selected_rows'),
     Input('dpdwn1','value'),
     Input('dpdwn2','value'),
    ]
)
def update_graphs(select_rows,dpd1,dpd2):
    #print(f'Selected Rows = {select_rows}')
    if(len(select_rows)==0):
        dfff = dff[dff['countriesAndTerritories'].isin(['India','China','Brazil','Pakistan'])]
    else:
        dfff = dff[dff['countriesAndTerritories'].index.isin(select_rows)]
    #display(dfff)
    
    selected = dfff['countriesAndTerritories'].tolist()
    dfl = df[df['countriesAndTerritories'].isin(selected)]
    #display(dfl)
    return(getLine(dfl,dpd1),getPie(dfff,dpd2))
    


if __name__=='__main__':
    app.run_server(host="0.0.0.0",debug=False, port = 8080)