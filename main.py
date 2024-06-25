from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
debug = True

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/blog')
def about():
    return render_template('about.html')

