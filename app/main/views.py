from flask import render_template

from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/page1')
def page1():
    return render_template('page1.html')


@main.route('/page2')
def page2():
    return render_template('page2.html')
