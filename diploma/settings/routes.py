from flask import render_template
from flask_login import login_required, current_user

from diploma.sensor.routes import get_by_user_id, get_status_list, get_sync_list, SensorStatus, SyncType
from diploma.settings import bp


@bp.route('/account')
@login_required
def account_settings():
    return render_template('settings/account.html', title='Account')


@bp.route('/sensor', methods=['GET'])
@login_required
def sensors_settings():
    sensors = get_by_user_id(current_user.get_id()).get_json()
    for sensor in sensors['sensors']:
        sensor['sync_type'] = SyncType(sensor['sync_type']).value
        sensor['status'] = SensorStatus(sensor['status']).value

    return render_template('settings/sensors.html',
                           title='Sensors',
                           sensors=sensors,
                           status_list=get_status_list().get_json(),
                           sync_list=get_sync_list().get_json(),
                           str=str)
