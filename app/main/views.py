from random import choice
from string import ascii_uppercase

from flask import render_template, redirect, url_for, make_response, request

from . import main
from ..models import User


@main.before_request
def before_request():
    cookie = request.cookies.get('user_id')
    if not cookie:
        cookie = ''.join(choice(ascii_uppercase) for i in range(32))
        resp = make_response(redirect(url_for('main.index', id=cookie)))
        resp.set_cookie('user_id', cookie)
        return resp

@main.route('/')
def index():
    id = request.cookies.get('user_id')
    if User.query.filter(User.id == id).first() is None:
        u = User(id=id)
        u.save()
    u = User.query.filter(User.id == id).first()
    return render_template('index.html', id=id, user=u)
