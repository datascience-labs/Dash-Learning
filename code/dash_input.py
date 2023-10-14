from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.Label('아이디:'),
    dcc.Input(id='id-input', type='text', placeholder='아이디를 입력하세요'),

    html.Label('비밀번호:'),
    dcc.Input(id='password-input', type='password', placeholder='비밀번호를 입력하세요'),

    html.Button('로그인', id='login-btn'),

    html.Div(id='output-div')
])


if __name__ == '__main__':
    app.run(debug=True)
