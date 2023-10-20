#/usr/bin/env sh

KB_LABEL="DACTYL"
USER_KM="user_keymaps/its-fonsy/main.py"
USER_BOARD="user_keymaps/its-fonsy"

# Give the user time to unplug the keyboard
timeout=3
echo "Unplug the keyboard"
while [ $timeout -ne 0 ]
do
    echo -ne "\rWaiting $timeout seconds"
    let timeout--
    sleep 1
done

# Wait for the KB to be plugged in
echo -ne "\nPlug the keyboard"
timeout=20
while [ -z "$BLOCK_PATH" ]
do
    # MCU isn't plugged in
    if [[ $timeout -eq 0 ]]; then
        echo "ERROR: can't find the MCU. Is it plugged in correctly?"
        exit 1
    fi

    BLOCK_PATH=$(lsblk -l -o PATH,LABEL | grep $KB_LABEL | cut -d" " -f1)
    let timeout--
    sleep 1
    echo -ne '.'
done

echo KEYBOARD DETECTED!

# For split keyboard distinguish left and right side
#KB_LABEL=$(lsblk -l -o LABEL | grep $KB_LABEL | cut -d" " -f1)

# If the drive isn't already mounted, mount it
BLOCK_MOUNTPOINT=$(lsblk -l -o MOUNTPOINT,LABEL | grep $KB_LABEL | cut -d" " -f1)
if [[ -z "$BLOCK_MOUNTPOINT" ]]; then
    udisksctl mount -b $BLOCK_PATH
    BLOCK_MOUNTPOINT=$(lsblk -l -o MOUNTPOINT,LABEL | grep $KB_LABEL | cut -d" " -f1)
fi

# Flash the files into the mcu
make MOUNTPOINT=$BLOCK_MOUNTPOINT USER_KEYMAP=$USER_KM BOARD=$USER_BOARD

udisksctl unmount -b $BLOCK_PATH

exit 0
