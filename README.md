# i3-config

Disclaimer.

## Installation

    pacaur -S i3-wm i3status feh xorg-xwininfo autocutsel pasystray \
      i3-lock caffeine-ng network-manager-gnome notify-osd \
      pavucontrol gnome-screensaver konsole

## Configuration

### Wallpaper

Expected at `~/.config/i3/wallpaper.png`.

### GTK Settings

.gtkrc-2.0

    include ".gtkrc-2.0-gnome-color-chooser"
    gtk-theme-name = "Clearlooks"
    gtk-font-name = "Sans 8"

.config/gtk-3.0/settings.ini

    [Settings]
    gtk-application-prefer-dark-theme=0
    gtk-theme-name = Adwaita
    gtk-font-name = Sans 8

### Gnome Keyring

    if [ -n "$PS1" ] && [ -z "$SSH_CONNECTION" ]; then
      eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,secrets,ssh)
      export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK
    fi

### Default Browser

    xdg-mime default firefox-trunk.desktop text/html
    xdg-mime default firefox-trunk.desktop x-scheme-handler/http
    xdg-mime default firefox-trunk.desktop x-scheme-handler/https
    xdg-mime default firefox-trunk.desktop x-scheme-handler/about

### Keyboard

/etc/X11/xorg.conf

    Section "InputClass"
      Identifier "evdev keyboard catchall"
      MatchIsKeyboard "on"
      MatchDevicePath "/dev/input/event*"
      Driver "evdev"
      Option  "XkbOptions"  "ctrl:nocaps,compose:caps,compose:rctrl,terminate:ctrl_alt_bksp"
    EndSection
