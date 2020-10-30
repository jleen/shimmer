import os
import time

from phue import Bridge

UPDATE_FREQUENCY = 2
STEPS = 5
DO_IT = True

bridge = Bridge(os.environ['PHUE_BRIDGE'])
bridge.connect()
lights = bridge.get_light_objects('name')

def get_light(n):
    return lights['Solarium ' + str(n+1)]

HUES = [get_light(i).hue for i in range(6)]
#HUES = [49189, 41107, 25600, 10909, 6980, 65155]
print('init:', HUES)

def interp(i, step):
    left = HUES[i % 6]
    right = HUES[(i + 1) % 6]
    diff = right - left
    if (0 < diff < 32768) or (diff < -32768):
        interp = left + (diff * step) // STEPS
    else:
        interp = left - (diff * step) // STEPS
    return (interp + 65536) % 65536

while True:
    for phase in range(6):
        for step in range(STEPS):
            hues = [interp((i + phase) % 6, step) for i in range(6)]
            if step == 0:
                print('p' + str(phase) + 's' + str(step) + ':', hues)
            if DO_IT:
                for i in range(6):
                    light = get_light(i)
                    light.hue = interp((i + phase) % 6, step)
            time.sleep(UPDATE_FREQUENCY)
