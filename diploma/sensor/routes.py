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
        return jsonify({'status': 'Failed', 'message': 'empty request'}), 400

    if 'region_key' not in data:
        coords = data['coordinates'].split(',')
        print(coords)
        weather = AccuWeatherAPI()
        region_info = weather.get_region_info(lat=coords[0], long=coords[1])
        data['region_key'] = region_info['Key']
        data['region_name'] = region_info['Country']['LocalizedName'] + ': ' + region_info['LocalizedName']

    if 'region_name' not in data:
        weather = AccuWeatherAPI()
        region_info = weather.get_region_info(region_key=data['region_key'])
        data['region_name'] = region_info['Country']['LocalizedName'] + ': ' + region_info['LocalizedName']

    if 'sync_type' not in data:
        data['sync_type'] = SyncType.EACH_DAY.value

    sensor = Sensor(
        user_id=current_user.get_id(),
        region_key=data['region_key'],
        region_name=data['region_name'],
        coordinates=data['coordinates'],
        status=SensorStatus.ACTIVE,
        sync_type=SyncType(data['sync_type'])
    )

    db.session.add(sensor)
    db.session.commit()

    return jsonify({'status': 'OK'})


@bp.route('/<int:sensor_id>', methods=['PUT'])
@login_required
def update(sensor_id):
    data = request.get_json()
    sensor = Sensor.query.filter_by(id=sensor_id).first()
    if not sensor:
        return jsonify({'status': 'Failed', 'message': 'No sensor with such id: {}'.format(sensor_id)}), 400

    if 'coordinates' in data:
        sensor.coordinates = data['coordinates']
    if 'region_name' in data:
        sensor.region_name = data['region_name']
    if 'region_key' in data:
        sensor.region_key = data['region_key']
    if 'sync_type' in data:
        sensor.sync_type = SyncType(data['sync_type'])
    if 'status' in data:
        sensor.status = SensorStatus(data['status'])
    if 'is_shared' in data:
        sensor.is_shared = data['is_shared']

    db.session.commit()
    return jsonify({'status': 'Success', 'sensor': sensor.as_dict()}), 200


@bp.route('/<int:sensor_id>', methods=['DELETE'])
@login_required
def delete(sensor_id):
    sensor = Sensor.query.filter_by(id=sensor_id).first()

    if not sensor:
        return jsonify({'status': 'Failed', 'message': 'No sensor with such id: {}'.format(sensor_id)}), 400

    Sensor.query.filter_by(id=sensor_id).delete()
    db.session.commit()

    return jsonify({'status': 'Success'}), 200


@bp.route('/all', methods=['GET'])
@login_required
def get_all():
    return jsonify(sensors=[s.as_dict() for s in Sensor.query.all()])


@bp.route('/region/<int:region_key>', methods=['GET'])
@login_required
def get_by_region_key(region_key):
    return jsonify(sensors=[s.as_dict() for s in Sensor.query.filter_by(region_key=region_key).all()])


@bp.route('/status-list', methods=['GET'])
def get_status_list():
    return jsonify(SensorStatus.as_dict())


@bp.route('/sync-list', methods=['GET'])
def get_sync_list():
    return jsonify(SyncType.as_dict())
