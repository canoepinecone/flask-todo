#!/usr/bin/env python

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'

@app.route('/')
def home_page():
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run()
