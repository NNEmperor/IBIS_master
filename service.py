from models import *



def get_compresor_value():
    return Compresor.value

def get_pneumatic_valve_value():
    return PneumaticValve.value

def get_sensor_value():
    return Sensor.value

def get_hand_valve_value(id):
    return HandValves.value[id]

def get_consumer_value(id):
    return Consumers.value[id]


def update_compresor_value(new_compresor_value):
    Compresor.value = new_compresor_value
    return Compresor.value

def update_pneumatic_valve_value(new_pneumatic_valve_value):
    PneumaticValve.value = new_pneumatic_valve_value
    return PneumaticValve.value

def update_hand_valve_value(id, new_hand_valve_value):
    HandValves.value[id] = new_hand_valve_value
    return HandValves.value[id]



