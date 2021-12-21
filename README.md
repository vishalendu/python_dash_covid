# python_dash_covid


The aim of this project is to demonstrate how a dataset can be viewed and graphed using Plotly's Dash Application
This is a complete application written in Python and doesnt require extensive knowledge of javascript and css.


Thanks to the creator of video mentioned in the References below, I have used his code and done minor changes to make it easier to code (specially for people who dont want to understand HTML/Divs.

The main structure of the HTML page for the app follows the following design
```
dbc.Container([
                  dbc.Row([
                            dbc.Col(html.H1)
                         ]),
                  dbc.Row([
                            dbc.Col([dash_table.DataTable)])
                          ]),
                  dbc.Row([
                            dbc.Col([dcc.Dropdown()]),
                            dbc.Col([dcc.Dropdown()])
                           ]),
                  dbc.Row([
                            dbc.Col([dcc.Graph()]),
                            dbc.Col([dcc.Graph()])
                          ])
             ])
```
Here you can see that the application layout is defined as simple to understand "Row" and "Col" objects. The actual objects like "DropDown". "DataTable" are very well documented on Plotly's documentation website, so it would be very trivial to replace them with whatever you need.
                            
                  
the second part of the code deals with attaching the data to the Graphs. The callbacks

@app.callback(
    [Output('lineplot', 'figure'),
     Output('piechart', 'figure')],
    [Input('datatable1', 'selected_rows'),
     Input('dpdwn1','value'),
     Input('dpdwn2','value'),
    ]
)
def func(3 inputs and 2 outputs)

The above callback decorator is used on a function which has to take as many inputs and provide as many outputs as mentioned in the decorator. 
This is pretty straight forward, as you can see the Input/Output element in the decorator have a touple of "compoment id" and component output for the ones to be used for input and output.

                  

References:
https://dash.plotly.com/datatable/reference
https://www.youtube.com/watch?v=dgV3GGFMcTc
