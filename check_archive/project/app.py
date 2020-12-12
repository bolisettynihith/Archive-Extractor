import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template, send_file, abort, jsonify
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['zip', 'tar', 'rar'])


@app.route('/check/<filename>')
def allowed_file(filename):
    if filename.split('.',1)[1].lower() in ALLOWED_EXTENSIONS:
        return jsonify({'check': True})
    else:
        return jsonify({'check': False})


if __name__ == "__main__":
    #app.secret_key = 'someaprghaerg'
    app.run(host='0.0.0.0',port=5001, debug=True)
