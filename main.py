from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')
