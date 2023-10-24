import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP13,  # column
    source=board.GP2,  # row
    keyboard=True,
    midi=False,
    mouse=False,
    storage=False,
    usb_id=('KMK Keyboards', 'Dactyl Mini 5x6'),
)
