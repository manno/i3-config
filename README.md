# i3-config

Disclaimer.

## Installation

    apt-get install i3 i3status \
      libpulse-dev \
      gmrun notification-daemon 

### Synapse

    apt-get install apt-get install libgee-0.8-dev libunique-3.0-dev libkeybinder-3.0-dev libjson-glib-dev libgee-dev libzeitgeist-dev valac        

### Wallpaper    

Expected at `~/.local/share/wallpaper.png`.

### Volume Control

#### ponymix

https://github.com/falconindy/ponymix

#### pactl

    apt-get install pulseaudio-utils


#### pa-applet

    apt-get install libglib2.0-dev libgtk-3-dev \
      libnotify-dev libpulse-dev libx11-dev \
      autoconf automake pkg-config

      
    git clone https://github.com/fernandotcl/pa-applet.git 

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

### Keyboard

/etc/X11/xorg.conf

    Section "InputClass"
      Identifier "evdev keyboard catchall"
      MatchIsKeyboard "on"
      MatchDevicePath "/dev/input/event*"
      Driver "evdev"
      Option  "XkbOptions"  "ctrl:nocaps,compose:caps,compose:rctrl,terminate:ctrl_alt_bksp"
    EndSection
