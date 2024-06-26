from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)
debug = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def work():
    return render_template('works.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/<username>')
def hello_world(username=None):
    numero = random.randint(1, 2000)
    return render_template('index.html', name=username, rad=numero)

# @app.route('/blog')
# def about():
#     return render_template('about.html')

@app.route('/bio')
def ale():#Endpoint criado
    numero = random.randint(1, 2000)
    numero2 = random.randint(1, 2000)
    numero3 = random.randint(1, 2000)
    dei = {'numero1':numero, 'numero2':numero2, 'numero3':numero3}
    return dei
