from flask import render_template
from flask_login import login_required, current_user

from diploma.sensor.routes import get_all, get_status_list, get_sync_list, SensorStatus, SyncType
from diploma.settings import bp


@bp.route('/account')
@login_required
def account_settings():
    return render_template('settings/account.html', title='Account')


@bp.route('/sensor')
@login_required
def sensors_settings():
    sensors = get_all().get_json()
    current_user_sensors = []
    for sensor in sensors['sensors']:
        if sensor['user_id'] == current_user.get_id():
            sensor['sync_type'] = SyncType(sensor['sync_type']).value
            sensor['status'] = SensorStatus(sensor['status']).value
            current_user_sensors.append(sensor)
    print(current_user_sensors)
    return render_template('settings/sensors.html',
                           title='Sensors',
                           sensors=current_user_sensors,
                           status_list=get_status_list().get_json(),
                           sync_list=get_sync_list().get_json(),
                           str=str)
