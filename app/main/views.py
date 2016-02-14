from random import choice, randint
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
    u = User.query.filter(User.id == id).first_or_404()
    return render_template('index.html', id=id, user=u)


@main.route('/_actions')
def _actions():
    u = User.query.filter(User.id == request.cookies.get('user_id')).first_or_404()
    return render_template('actions.html', user=u)


@main.route('/_events')
def _events():
    u = User.query.filter(User.id == request.cookies.get('user_id')).first_or_404()
    return render_template('events.html', events=u.event_stream)

@main.route('/_inventory')
def _inventory():
    u = User.query.filter(User.id == request.cookies.get('user_id')).first_or_404()
    return render_template('inventory.html', user=u)


@main.route('/_get_action/<id>')
def _get_action(id):
    u = User.query.filter(User.id == request.cookies.get('user_id')).first_or_404()

    if id == 'Get_Wood':
        r = randint(0, 10);
        u.wood += r
        u.unlock('Find_Flint')
        r <= 2
    elif id == 'Find_Flint'
        r = randint(0, 5)
        u.flint += r
    elif id == 'Explore':

    elif id == 'Find_Stone':
        r = randint(0, 5)
        u.stone += r
    elif id == 'Start_Fire':

    elif id == 'Harvest_Apples':
        r = randint(1, 7)
        u.apple += r
    return ''
