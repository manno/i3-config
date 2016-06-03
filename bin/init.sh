#!/bin/sh

xinput set-prop 'AlpsPS/2 ALPS DualPoint TouchPad' 'Device Enabled' 0
xinput set-prop 'AlpsPS/2 ALPS DualPoint TouchPad' 'Synaptics Off' 1

xrandr --output eDP1 --primary
~/.config/i3/bin/awsetbg /usr/share/wallpapers/openSUSEdefault/contents/images/1920x1080.jpg
