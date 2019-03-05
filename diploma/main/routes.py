import os

from flask import send_from_directory, render_template, current_app
from flask_login import login_required

from diploma.main import bp
from subscriber import subscribe


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@bp.route('/subscribe')
def subscribe():
    current_app.task_queue.enqueue(subscribe)
    return render_template('index.html', title='Home')


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')
