from dash import Dash, dcc, html, Input, Output,callback

app = Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(['서울', '부산', '울산'], '부산', id='demo-dropdown'),
    html.Div(id='select')
])


@callback(
    Output('select', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'선택된 도시: {value}'


if __name__ == '__main__':
    app.run(debug=True)
