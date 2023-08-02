#/usr/bin/env sh

KB_LABEL="DACTYL"
USER_KM="user_keymaps/its-fonsy/main.py"
USER_BOARD="user_keymaps/its-fonsy"

BLOCK_PATH=$(lsblk -l -o PATH,LABEL | grep $KB_LABEL | cut -d" " -f1)
BLOCK_MOUNTPOINT=$(lsblk -l -o MOUNTPOINT,LABEL | grep $KB_LABEL | cut -d" " -f1)

# Check if the USB stick is plugged in
if [[ -z "$BLOCK_PATH" ]]; then
    echo "ERROR: can't find the MCU. Is it plugged in correctly?"
    exit 1
fi

# For split keyboard distinguish left and right side
KB_LABEL=$(lsblk -l -o LABEL | grep $KB_LABEL | cut -d" " -f1)

# If the drive isn't already mounted, mount it
if [[ -z "$BLOCK_MOUNTPOINT" ]]; then
    udisksctl mount -b $BLOCK_PATH
    BLOCK_MOUNTPOINT=$(lsblk -l -o MOUNTPOINT,LABEL | grep $KB_LABEL | cut -d" " -f1)
fi

# Flash the files into the mcu
make MOUNTPOINT=$BLOCK_MOUNTPOINT USER_KEYMAP=$USER_KM BOARD=$USER_BOARD

udisksctl unmount -b $BLOCK_PATH

exit 0
