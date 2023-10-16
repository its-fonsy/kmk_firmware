from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide
from storage import getmount

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

if side == SplitSide.RIGHT:
    uart_pin = keyboard.uart_tx
else:
    uart_pin = keyboard.uart_rx

split = Split(
    data_pin = uart_pin
)

keyboard.modules.append(split)

keyboard.keymap = [
    [   # 0
        KC.ESC,  KC.N1,   KC.N2,   KC.N3, KC.N4,   KC.N5,                                 KC.N6, KC.N7,   KC.N8,   KC.N9,   KC.N0,  KC.GRV,
        KC.CAPS,  KC.Q,    KC.W,    KC.E,  KC.R,    KC.T,                                  KC.Y,  KC.U,    KC.I,    KC.O,    KC.P, KC.BSLS,
        KC.LSFT,  KC.A,    KC.S,    KC.D,  KC.F,    KC.G,                                  KC.H,  KC.J,    KC.K,    KC.L, KC.SCLN, KC.RSFT,
        KC.LCTL,  KC.Z,    KC.X,    KC.C,  KC.V,    KC.B,                                  KC.N,  KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RCTL,
                        KC.LEFT, KC.RGHT,           KC.Q, KC.SPC, KC.W,      KC.Q, KC.ENT, KC.D,          KC.UP, KC.DOWN,
                                                            KC.E, KC.S,      KC.W,   KC.S,
    ],
]

if __name__ == '__main__':
    keyboard.go()
