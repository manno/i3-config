#!/bin/sh
# Touchpad disable, in absence of g-s
xinput set-prop "SynPS/2 Synaptics TouchPad" "Device Enabled" 0
xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation" 1
xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Button" 2

