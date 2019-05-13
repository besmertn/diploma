from datetime import datetime

from flask import render_template, request, jsonify
from flask_login import login_required

from diploma import db
from diploma.models import Record
from diploma.sensor.routes import available_sensors
from diploma.statistic import bp


@bp.route('/')
@login_required
def index():
    # date_range = {'from': datetime.today(), 'to': datetime.today() + timedelta(days=10)}
    data = parse_data(Record.query.filter(Record.sensor_id.in_({s.id for s in available_sensors()})).all())
    return render_template('statistic/index.html', title='Statistic', data=data)


@bp.route('/add', methods=['POST'])
def add_record():
    data = request.get_json()

    if not data:
        return jsonify({'status': 'Failed', 'message': 'empty request'}), 400

    if 'sensor_id' not in data or 'timestamp' not in data:
        return jsonify({'status': 'Failed', 'message': 'missing sensor_id or timestamp fields'}), 400

    record = Record(
        sensor_id=data['sensor_id'],
        timestamp=datetime.fromtimestamp(data['timestamp']),
        pm10=data['pm10'],
        pm25=data['pm25'],
        temperature=data['temperature'],
        humidity=data['humidity'],
        rainfall=data['rainfall']
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({'status': 'OK'})


@bp.route('/<int:region_key>', methods=['GET'])
def get_by_region(region_key):
    sensor_id_list = {s.id for s in available_sensors() if s.region_key == region_key}
    records = Record.query.filter(Record.sensor_id.in_(sensor_id_list)).all()
    return render_template('statistic/index.html', title='Statistic', data=parse_data(records))


@bp.route('/date', methods=['POST'])
def get_by_date_range():
    date_range = request.get_json()
    if 'from' not in date_range or 'to' not in date_range:
        return jsonify({'status': 'Failed', 'message': 'missing \'from\' or \'to\' value'}), 400

    from_datetime = datetime.strptime(date_range['from'], '%m/%d/%y, %I:%M %p')
    to_datetime = datetime.strptime(date_range['to'], '%m/%d/%y, %I:%M %p')

    records = Record.query.filter(Record.sensor_id.in_({s.id for s in available_sensors()})).all()
    filtered_records = {d for d in records if from_datetime <= d.timestamp <= to_datetime}
    filtered_records = list(filtered_records)
    return jsonify(data=parse_data(filtered_records)), 200


def parse_data(data):
    data.sort(key=lambda x: x.timestamp, reverse=False)
    result = [['Day', 'PM10', 'PM2.5', 'Temperature', 'Humidity']]
    for i in data:
        result.append([str(i.timestamp), i.pm10, i.pm25, i.temperature, i.humidity])

    return result
