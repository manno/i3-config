# i3-config

Disclaimer.

## Installation

    apt-get install libpulse-dev nitrogen

### Wallpaper    

Expected at `~/.local/share/wallpaper.png`.

### Volume Control

https://github.com/falconindy/ponymix

### Keyring

Add to `.profile`

    eval `/usr/bin/gnome-keyring-daemon -s`
    export SSH_AUTH_SOCK
    export GPG_AGENT_INFO

### Compose Key

    setxkbmap -option compose:caps
