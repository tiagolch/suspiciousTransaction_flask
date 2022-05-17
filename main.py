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
        file.save(os.path.join(app.config['UPLOAD_FOLDER']) + filename)
        print(f'Arquivo: {filename} Tamanho: {os.path.getsize(app.config["UPLOAD_FOLDER"] + filename)}')
        return f'{filename} de tamanho {os.path.getsize(app.config["UPLOAD_FOLDER"] + filename)} bytes Importado com sucesso!', 200
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
