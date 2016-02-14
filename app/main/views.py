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
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/play')
def play():
    id = request.cookies.get('user_id')
    if User.query.filter(User.id == id).first() is None:
        u = User(id=id)
        u.save()
    u = User.query.filter(User.id == id).first_or_404()
    return render_template('play.html', id=id, user=u)


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
    if id == 'Explore':
        # TODO: FINISH ME!
        u.log_event('You wander aimlessly through the woods.')
        r = randint(1, 10)
        if r <= 2:
            u.log_event('You stumble upon some fallen sticks (+2 Wood)')
            u.wood += 2
        if r <= 8:
            u.log_event('You gather some plat matter (+10 Weeds)')
            u.weeds += 10
        u.save()
    elif id == 'Get_Wood':
        r1 = randint(5, 10)
        u.wood += r1
        u.log_event('You gather some wood in the forest (+%s Wood)' % str(r1))
        r2 = randint(0, 10)
        if r2 <= 2:
            u.log_event('You gather some small stones as you collect the wood (+2 Stone)')
            u.stone += 2
            u.Find_Stone = True
            u.save()
        u.save()
    elif id == 'Find_Stone':
        r1 = randint(0, 10)
        u.stone += r1
        u.log_event('You gather some stones from the riverbank. (+%s Stone)' % r1)
        r2 = randint(0, 10)
        if r2 <= 3:
            u.log_event('You find a piece of flint in the stone (+%s Flint)' % r2)
            u.flint += 2
            u.Find_Flint = True
        u.save()
    elif id == 'Find_Flint':
        r1 = randint(0, 3)
        u.flint += r1
        u.log_event('You dig through the gravel, looking for flint. (+%s Flint)' % r1)
        r2 = randint(0, 10)
        if r2 <= 2:
            u.log_event('You find a rusty old hatchet in the gravel. It appears to be made of steel. (+1 Hatchet)')
            u.hatchets += 1
            u.Start_Fire = True
        u.save()
    elif id == 'Start_Fire':
        if u.flint >= 5 and u.hatchets >= 1 and u.wood >= 25:
            u.flint -= 5
            u.hatchets -= 1
            u.wood -= 25
            u.log_event(
                'You create a small fire by striking a flint stone against the hatchet. It blossoms into a warm flame as you add wood. (-5 flint, -1 hatchet, -25 wood)')
        else:
            u.log_event('You need 5 flint and 1 hatchet to create this.')
        u.save()
    return ''
