from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.capsword import CapsWord
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.modules.split import Split, SplitSide
from storage import getmount

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(TapDance())
keyboard.modules.append(CapsWord())

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

if side == SplitSide.RIGHT:
    uart_pin = keyboard.uart_tx
else:
    uart_pin = keyboard.uart_rx

split = Split( data_pin = uart_pin )

keyboard.modules.append(split)

# HoldTap keys
CTL_ESC = KC.HT(KC.ESC, KC.LCTRL)
CTL_TAB = KC.HT(KC.TAB,  KC.RCTRL)

SFT_ENT = KC.HT(KC.ENT, KC.RSFT, tap_time=200, prefer_hold=False)
SFT_SPC = KC.HT(KC.SPC, KC.LSFT, tap_time=200, prefer_hold=False)

GUI_DEL = KC.HT(KC.DEL, KC.LGUI)
GUI_BSP = KC.HT(KC.BSPC, KC.RGUI)

ALT_PLS = KC.HT(KC.PLUS, KC.RALT)
ALT_UND = KC.HT(KC.UNDS, KC.RALT)

L1_BSLS = KC.LT(1, KC.BSLS) 
L2_PIPE = KC.LT(2, KC.PIPE) 

# TapDance keys
LBRC_LCBR = KC.TD(KC.LBRC, KC.LCBR)
RBRC_RCBR = KC.TD(KC.RBRC, KC.RCBR)

XXXXXXX = KC.TRNS

keyboard.keymap = [
    [   # Layer 0
        KC.LSFT,    KC.N1,   KC.N2,   KC.N3, KC.N4,   KC.N5,                                             KC.N6, KC.N7,   KC.N8,   KC.N9,   KC.N0, KC.PGUP,
        KC.CAPS,     KC.Q,    KC.W,    KC.E,  KC.R,    KC.T,                                              KC.Y,  KC.U,    KC.I,    KC.O,    KC.P, KC.TILD,
         KC.GRV,     KC.A,    KC.S,    KC.D,  KC.F,    KC.G,                                              KC.H,  KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,
          KC.CW,     KC.Z,    KC.X,    KC.C,  KC.V,    KC.B,                                              KC.N,  KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.PGDW,
                           KC.MINS, ALT_PLS,        GUI_DEL, SFT_SPC,   L1_BSLS,     L2_PIPE, SFT_ENT, GUI_BSP,        ALT_UND,  KC.EQL,
                                                             CTL_ESC, LBRC_LCBR,   RBRC_RCBR, CTL_TAB,
    ],
    [   # Layer 1
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, XXXXXXX,                                          KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                          XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX,  XXXXXXX,     XXXXXXX, XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX,
                                                              XXXXXXX,  XXXXXXX,     XXXXXXX, XXXXXXX,
    ],
    [   # Layer 2
        XXXXXXX,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,                                            KC.F6,   KC.F7,   KC.F8,   KC.F9,  KC.F10,  KC.F11,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  KC.F12,
        XXXXXXX, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, XXXXXXX,                                          XXXXXXX, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                          XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX,  XXXXXXX,     XXXXXXX, XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX,
                                                              XXXXXXX,  XXXXXXX,     XXXXXXX, XXXXXXX,
    ],
]

"""
Blank Layer template

[   # Layer X
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                      XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX,  XXXXXXX,     XXXXXXX, XXXXXXX, XXXXXXX,          XXXXXXX, XXXXXXX,
                                                          XXXXXXX,  XXXXXXX,     XXXXXXX, XXXXXXX,
],
"""

if __name__ == '__main__':
    keyboard.go()
