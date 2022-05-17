import os
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd() + '/templates/static/files/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER']) + filename)
        return filename, 200
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
