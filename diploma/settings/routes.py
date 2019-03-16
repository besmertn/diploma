from flask import render_template
from flask_login import login_required

from diploma.settings import bp


@bp.route('/account')
@login_required
def account_settings():
    return render_template('settings/account.html', title='Account')


@bp.route('/sensor')
@login_required
def sensors_settings():
    return render_template('settings/sensors.html', title='Sensors')
