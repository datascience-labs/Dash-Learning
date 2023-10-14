# 필요한 기능 가져오기
from dash import Dash, html
from dash.dependencies import Input, Output

app = Dash(__name__)

# 앱 레이아웃 설계
app.layout = html.Div([
    html.Button(children='Click me!', id='my-button'),
    html.Div(id='my-output')
])

# 콜백 정의
@app.callback(
    Output('my-output', 'children'),
    Input('my-button', 'n_clicks')
)
# 콜백 함수 동작 설계
def update_output(n_clicks):
    if n_clicks:
        return f'버튼이 {n_clicks} 번 클릭 되었습니다!'
    else:
        return '버튼이 아직 클릭 되지 않았습니다.'

# 앱 실행
if __name__ == '__main__':
    app.run_server(debug=True)




