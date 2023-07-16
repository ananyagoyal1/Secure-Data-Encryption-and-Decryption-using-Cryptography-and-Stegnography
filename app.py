from flask import Flask, render_template, request
import os
from base_enc import base_enc
from base_dec import base_dec
from werkzeug.utils import secure_filename
from rsa_enc import rsa_enc 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/coverimages'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Encryption')
def encrypt():
    return render_template('encryption.html')

@app.route('/Decryption')
def decrypt():
    return render_template('decryption.html')

@app.route('/Encryption', methods=['POST'])
def getdata_enc():
    source_file = request.files['source_file']
    p = int(request.form['prime_1'])
    q = int(request.form['prime_2'])
    cover_file = request.files['cover_file']
    new_img_name = secure_filename(request.form['new_name'])

    source_name = os.path.join(app.config['UPLOAD_FOLDER'], source_file.filename)
    source_file.save(source_name)

    cover_name = os.path.join(app.config['UPLOAD_FOLDER'], cover_file.filename)
    cover_file.save(cover_name)

    base_enc(source_name)

    rsa_enc(p, q, source_name)

    return render_template('thank.html')

@app.route('/Decryption', methods=['POST'])
def getdata_dec():
    cover_file = request.files['cover_file']
    p = int(request.form['prime_1'])
    q = int(request.form['prime_2'])
    new_cover_name = request.form['new_cover_name']

    cover_name = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(cover_file.filename))
    cover_file.save(cover_name)

    base_dec(new_cover_name)

    rsa_dec(p, q)

    return render_template('thank.html')


if __name__ == '__main__':
    app.run(debug=True)
