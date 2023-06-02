from flask import Flask, render_template, request, jsonify
import random
import requests
from waitress import serve
import webbrowser
import base64



app = Flask(__name__)
app.debug = True

@app.route('/')
def quiz():
    danxuan_encoded_url="aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0RlZmVuc2l2ZVNuaXBlci90ZXN0L21haW4vZGFueHVhbi5qc29u"
    danxuan_decoded_url = base64.b64decode(danxuan_encoded_url).decode()
    danxuan_url = danxuan_decoded_url
    danxuan_response = requests.get(danxuan_url)
    danxuan_data = danxuan_response.json()

    duoxuan_encoded_url="aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0RlZmVuc2l2ZVNuaXBlci90ZXN0L21haW4vZHVveHVhbi5qc29u"
    duoxuan_decoded_url = base64.b64decode(duoxuan_encoded_url).decode()
    duoxuan_url = duoxuan_decoded_url
    duoxuan_response = requests.get(duoxuan_url)
    duoxuan_data = duoxuan_response.json()

    panduan_encoded_url="aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0RlZmVuc2l2ZVNuaXBlci90ZXN0L21haW4vcGFuZHVhbi5qc29u"
    panduan_decoded_url = base64.b64decode(panduan_encoded_url).decode()
    panduan_url = panduan_decoded_url
    panduan_response = requests.get(panduan_url)
    panduan_data = panduan_response.json()

    selected_danxuan = random.sample(danxuan_data, 50)
    selected_duoxuan = random.sample(duoxuan_data, 30)
    selected_panduan = random.sample(panduan_data, 20)

    selected_questions = selected_danxuan + selected_duoxuan + selected_panduan

    return render_template('quiz.html', questions=selected_questions)

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.json.get('answer')
    correct_answer = request.json.get('correct_answer')

    return jsonify({'correct': answer == correct_answer})

if __name__ == '__main__':
    print("这个窗口千万别关闭！！！！！！")
    print("如果没有自动打开网页，请用浏览器打开http://127.0.0.1:8080/")
    print("这个窗口千万别关闭！！！！！！")
    print("如果没有自动打开网页，请用浏览器打开http://127.0.0.1:8080/")
    print("这个窗口千万别关闭！！！！！！")
    print("如果没有自动打开网页，请用浏览器打开http://127.0.0.1:8080/")
    print("如果运行错误，安装requirements.txt中所需要的依赖")
    webbrowser.open("http://127.0.0.1:8080/")

    serve(app, host="127.0.0.1", port=8080)