from flask import Blueprint, jsonify, request

from models import UpdateValue

api_bp = Blueprint('api', __name__)

@api_bp.route('/compresor', methods=['GET'])
def get_compresor():
    # get value from static variables/in memory db
    return jsonify(value = 1.0)

@api_bp.route('/compresor', methods=['PUT'])
def update_compresor():
    data = request.get_json()
    compresor_data = UpdateValue(data['id'], data['new_value'])
    # based on id
    # update value
    return jsonify(value = compresor_data.new_value)

@api_bp.route('/pneumatic_valve')
def get_pneumatic_valve():
    # get value from static variables/in memory db
    return jsonify(value = 1.0)

@api_bp.route('/pneumatic_valve', methods=['PUT'])
def update_pneumatic_valve():
    data = request.get_json()
    pneumatic_valve_data = UpdateValue(data['id'], data['new_value'])
    # based on id
    # update value
    return jsonify(value = pneumatic_valve_data.new_value)

@api_bp.route('/hand_valve', methods=['GET'])
def get_hand_valve():
    id = request.args.get('id')
    # based on id
    # get value from static variables/in memory db
    return jsonify(value = 1.0)

@api_bp.route('/hand_valve', methods=['PUT'])
def update_hand_valve():
    data = request.get_json()
    hand_valve_data = UpdateValue(data['id'], data['new_value'])
    # based on id
    # update value in static variables/in memory db
    return jsonify(value = hand_valve_data.new_value)

@api_bp.route('/sensor')
def get_sensor():
    # get value from static variables/in memory db
    return jsonify(value = 1.0)

@api_bp.route('/consumer', methods=['GET'])
def get_user():
    id = request.args.get('id')
    # based on id
    # get value from static variables/in memory db
    return jsonify(value = 1.0)