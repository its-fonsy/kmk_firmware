import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
    )
    col_pins = (
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
    )
    diode_orientation = DiodeOrientation.COL2ROW
    uart_tx = board.GP0
    uart_rx = board.GP1
    # flake9: noqa
    # fmt: off
    coord_mapping = [
         0,  1,  2,  3,  4,  5,                    36, 37, 38, 39, 40, 41,
         6,  7,  8,  9, 10, 11,                    42, 43, 44, 45, 46, 47,
        12, 13, 14, 15, 16, 17,                    48, 49, 50, 51, 52, 53,
        18, 19, 20, 21, 22, 23,                    54, 55, 56, 57, 58, 59,
                26, 27,     28, 35, 33,    66, 60, 61,     62, 63,
                                34, 32,    67, 68
    ]

"""
col         0   1   2   3   4   5
GPIO        8   9  10  11  12  13
          ------------------------
    row
GP2  0   |  0,  1,  2,  3,  4,  5,                    36, 37, 38, 39, 40, 41,
GP3  1   |  6,  7,  8,  9, 10, 11,                    42, 43, 44, 45, 46, 47,
GP4  2   | 12, 13, 14, 15, 16, 17,                    48, 49, 50, 51, 52, 53,
GP5  3   | 18, 19, 20, 21, 22, 23,                    54, 55, 56, 57, 58, 59,
GP6  4   |         26, 27,     28, 29, 35,    66, 60, 61,     62, 63,
GP7  5   |                         33, 34,    67, 68
"""
