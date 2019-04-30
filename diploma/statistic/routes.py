from flask import render_template
from flask_login import login_required

from diploma.statistic import bp


@bp.route('/')
@login_required
def index():
    data = [
        ['Day', 'PM10', 'PM2.5'],
        [1, 10, 25],
        [2, 12, 40],
        [3, 25, 39],
        [4, 13, 35],
        [5, 17, 36],
        [6, 11, 41],
        [7, 10, 20]
    ]
    return render_template('statistic/index.html', title='Statistic', data=data)
