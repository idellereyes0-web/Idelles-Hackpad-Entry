from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rotary_encoder import RotaryEncoder

from board import GP1, GP2, GP3, GP4, GP26, GP27, GP28

keyboard = KMKKeyboard()

# Pins for 4 buttons + rotary encoder switch(S1)
keyboard.col_pins = (GP3, GP4, GP2, GP1, GP28)
keyboard.row_pins = ()

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap: 4 buttons + encoder switch (S1)
# Map buttons to custom key combos using KC.LCTL, KC.LALT, and normal keys
keyboard.keymap = [
    [
        KC.LCTL(KC.LALT(KC.P)),  # Button 1: Ctrl + Alt + P
        KC.LCTL(KC.LALT(KC.K)),  # Button 2: Ctrl + Alt + K
        KC.LCTL(KC.C),           # Button 3: Ctrl + C
        KC.LCTL(KC.V),           # Button 4: Ctrl + V
        KC.MUTE                 # Rotary encoder switch (S1): Mute
    ],
]

# Rotary encoder pins (A and B)
encoder = RotaryEncoder(clock_pin=GP27, data_pin=GP26)

# Rotary encoder rotation
def encoder_rotate(direction):
    if direction > 0:
        keyboard.tap_code(KC.VOLU)  # Clockwise turn = volume up
    else:
        keyboard.tap_code(KC.VOLD)  # Counter-clockwise turn = volume down

encoder.rotate = encoder_rotate

keyboard.extensions.append(encoder)

if __name__ == "__main__":
    keyboard.go()
