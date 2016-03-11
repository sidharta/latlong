#! /usr/bin/env python

import os

from google.appengine.api import channel

from flask.ext.script import Manager
from flask import render_template

from app import create_app

app = create_app(os.getenv('APP_CONFIG', 'default'))
manager = Manager(app)
main_channel = channel.create_channel("latlong")

@app.route('/', methods=['GET'])
def home( ):
    return render_template('home.html', channel_id=main_channel)


@app.route('/history/<key>', methods=['GET'])
def history( key ):
    return render_template('history.html', key=key)

@manager.shell
def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()
