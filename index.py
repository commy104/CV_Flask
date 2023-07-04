from flask import Flask
from flask import render_template
# import __ import models

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/translate', methods=['POST'])
def translate():
    return


if __name__ == '__main__':
    app.run()
