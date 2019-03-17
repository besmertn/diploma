from flask import request, jsonify
from flask_login import login_required, current_user

from diploma import db
from diploma.main.accuweather import AccuWeatherAPI
from diploma.models import Sensor, SensorStatus, SyncType
from diploma.sensor import bp


@bp.route('/create', methods=['POST'])
@login_required
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'empty request'})

    if 'region_key' not in data:
        coords = data['coordinates'].split(',')
        print(coords)
        weather = AccuWeatherAPI()
        region_key = weather.get_location_key(lat=coords[0], long=coords[1])
        data['region_key'] = region_key

    if 'sync_type' not in data:
        data['sync_type'] = SyncType.EACH_DAY.value

    sensor = Sensor(
        user_id=current_user.get_id(),
        region_key=data['region_key'],
        coordinates=data['coordinates'],
        status=SensorStatus.ACTIVE,
        sync_type=SyncType(data['sync_type'])
    )

    db.session.add(sensor)
    db.session.commit()

    return jsonify({'status': 'OK'})


@bp.route('/all', methods=['GET'])
def get_all():
    return jsonify(sensors=[s.as_dict() for s in Sensor.query.all()])


@bp.route('/region/<int:region_key>', methods=['GET'])
def get_by_region_key(region_key):
    return jsonify(sensors=[s.as_dict() for s in Sensor.query.filter_by(region_key=region_key).all()])
