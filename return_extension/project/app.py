#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template, send_file, abort, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024


@app.route('/retext/<filename>')
def retext(filename):
    extension = filename.split(".",1)[1]
    return jsonify({'extension':extension})

if __name__ == "__main__":
    #app.secret_key = 'someaprghaerg'
    app.run(host='0.0.0.0',port=5002, debug=True)
