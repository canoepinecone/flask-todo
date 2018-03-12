#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_text = db.Column(db.String(1000), unique=True, nullable=False)

    def __init__(self, todo_text):
        self.todo_text = todo_text

    def __repr__(self):
        return '<Todo %r>' % self.todo_text

if not os.path.isfile('temp.db'):
    db.create_all()
    todo = Todo("Add todos")
    db.session.add(todo)
    db.session.commit()

@app.route('/')
def home_page():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/addtodo', methods=["POST"])
def add_todo():
    todo = Todo(request.form["todoText"])
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    app.run()
