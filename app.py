from flask import Flask, render_template
import env
from proctitle import setproctitle

setproctitle.setproctitle(env.PROC_NAME)

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    nav_item = (
        "Introduce", "portfolio", "Projecting", "Making Film", "Brand"
    )
    return render_template('index.html', nav_item=nav_item)


@app.route('/consulting_jang')
def consultingjang():
    return render_template('consultingjang.html')


@app.route('/edu_jang')
def edujang():
    nav_item = (
        "Introduce", "Review", "portfolio", "Brand"
    )
    return render_template('edujang.html', nav_item=nav_item)


@app.route('/volunteer_jang')
def volunteerjang():
    return render_template('volunteerjang.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=env.DEBUG, port=env.PORT)
