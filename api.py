from flask import Blueprint, jsonify, request
from service import *



api_bp = Blueprint('api', __name__)


@api_bp.route('/compresor', methods=['GET'])
def get_compresor():
    return jsonify(value = get_compresor_value())

@api_bp.route('/pneumatic_valve')
def get_pneumatic_valve():
    return jsonify(value = get_pneumatic_valve_value())

@api_bp.route('/sensor')
def get_sensor():
    return jsonify(value = get_sensor_value())

@api_bp.route('/hand_valve', methods=['GET'])
def get_hand_valve():
    id = request.args.get('id')
    return jsonify(value = get_hand_valve_value(id))

@api_bp.route('/consumer', methods=['GET'])
def get_user():
    id = request.args.get('id')
    return jsonify(value = get_consumer_value(id))


@api_bp.route('/compresor', methods=['PUT'])
def update_compresor():
    data = request.get_json()
    return jsonify(value = update_compresor_value(data['new_value']))

@api_bp.route('/pneumatic_valve', methods=['PUT'])
def update_pneumatic_valve():
    data = request.get_json()
    return jsonify(value = update_pneumatic_valve_value(data['new_value']))

@api_bp.route('/hand_valve', methods=['PUT'])
def update_hand_valve():
    data = request.get_json()
    return jsonify(value = update_hand_valve_value(data['id'], data['new_value']))