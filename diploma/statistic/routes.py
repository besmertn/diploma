from datetime import datetime

from flask import render_template, request, jsonify
from flask_login import login_required

from diploma import db
from diploma.models import Record
from diploma.statistic import bp


@bp.route('/')
@login_required
def index():
    data = [
        ['Day', 'PM10', 'PM2.5'],
        [1, 10, 15],
        [2, 12, 30],
        [3, 25, 29],
        [4, 13, 25],
        [5, 17, 26],
        [6, 11, 31],
        [7, 10, 20],
        [8, 12, 23.5],
        [9, 11.5, 22],
        [10, 18, 16],
        [11, 11.9, 13],
        [12, 19.1, 18.5],
        [13, 12, 23.5],
        [14, 13, 19.7],
        [15, 15.1, 20],
        [16, 14, 31.5],
        [17, 21, 19.59],
        [18, 11.78, 16]
    ]
    # Record.query.filter_by(region_key=region_key)
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
