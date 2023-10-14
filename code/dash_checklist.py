from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children="OO 설문조사",id='select'),
    html.Div(children="성별"),
    dcc.Checklist(
    ['남자', '여자', '비밀'] # 선택 옵션
),
    html.Div(children="연령"),
    dcc.Checklist(
    ['20대', '30대', '40대', '50대'], # 선택 옵션
    ['20대'] # 기본 선택 옵션
),
    html.Div(children="지역"),
    dcc.Checklist(
    ['서울', '부산', '울산'] # 선택 옵션

),
])


if __name__ == '__main__':
    app.run(debug=True)
