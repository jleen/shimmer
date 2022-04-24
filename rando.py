import os
import random
import time

from phue import Bridge

LIGHT_NAMES = [ 'Couch left', 'Couch right' ]
UPDATE_FREQUENCY = 5

bridge = Bridge(os.environ['PHUE_BRIDGE'])
bridge.connect()
lights = bridge.get_light_objects('name')

while True:
    desired = random.randint(0,65535)
    for light in [lights[name] for name in LIGHT_NAMES]:
        if light.on:
            light.hue = desired
            light.sat = 254
    time.sleep(UPDATE_FREQUENCY)
