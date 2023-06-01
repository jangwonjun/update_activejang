from flask import Flask, render_template
import env
from proctitle import setproctitle

setproctitle.setproctitle(env.PROC_NAME)

app  = Flask(__name__, static_url_path='/static')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/consulting_jang')
def consultingjang():
    return render_template('consultingjang.html')

@app.route('/edu_jang')
def edujang():
    return render_template('edujang.html')

@app.route('/volunteer_jang')
def volunteerjang():
    return render_template('volunteerjang.html')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=env.DEBUG, port=env.PORT)