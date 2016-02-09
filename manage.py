#!/usr/bin/env python
import os

from flask.ext.script import Manager, Shell

from app import create_app, db

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    # creates shell in app context (useful for db debugging)
    return dict(app=app, db=db)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
