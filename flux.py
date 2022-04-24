desired_state = None
previous_state = None

if light.on:
    if light.state == previous_state:
        light.set_state(desired_state):
else:
    light.set_button_function(desired_state)
