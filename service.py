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
    update_consumer_values()
    return Compresor.value

def update_pneumatic_valve_value(new_pneumatic_valve_value):
    PneumaticValve.value = new_pneumatic_valve_value
    update_consumer_values()
    return PneumaticValve.value

def update_hand_valve_value(id, new_hand_valve_value):
    HandValves.value[id] = new_hand_valve_value
    main_pressure = Compresor.value * PneumaticValve.value
    new_consumer_value = main_pressure * HandValves.value[id]
    update_consumer_value(id,new_consumer_value)
    return HandValves.value[id]

def update_consumer_value(id,new_consumer_value):
    Consumers.value[id] = new_consumer_value

def update_consumer_values():
    for x in range(4):
        new_consumer_value = Compresor.value * PneumaticValve.value * HandValves.value[x]
        update_consumer_value(x,new_consumer_value)


