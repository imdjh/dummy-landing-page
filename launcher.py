#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
# Serve the dummy landing-page.

from flask import Flask, render_template

# fire up our flask app ;)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def launchindex():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
