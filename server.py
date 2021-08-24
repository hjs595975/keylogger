from flask import Flask, request
from datetime import date,datetime #from에서 모듈 불러오기

app = Flask(__name__)#앱을 지정(변수)

@app.route('/get_logs', methods=['POST'])#로그를얻어서 post로 보내기
def get_logs():
    logs = request.form['logs']

    with open('logs.txt', 'a') as f:
        f.write(f'{datetime.now()} - {logs}\n')#시간까지 입력해서 로그받기

        return {'result': True}

if __name__ == '__main__':#메인으로 하기
    app.run(host='0.0.0.0')#여기서 실행