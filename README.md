# i3-config

Disclaimer.

## Installation

    apt-get install i3 i3lock i3status \
      libpulse-dev \
      nitrogen xautolock \
      gmrun synapse notification-daemon 

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

### Gnome Keyring

Add to `.profile`

    eval `/usr/bin/gnome-keyring-daemon -s`
    export SSH_AUTH_SOCK
    export GPG_AGENT_INFO

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

### Lock screen on suspend

/etc/pm/sleep.d/99local-i3lock:

    #!/bin/sh
    #
    # i3lock screen

    umask 022;
    PATH="$PATH:/usr/bin/X11"

    getXuser() {
      user=$(who | awk "/:$displaynum/ { print \$1; exit }")

      if [ x"$user" = x"" ]; then
        user=$(who | awk "/:$displaynum/ { print \$1; exit }")
      fi
      if [ x"$user" != x"" ]; then
        userhome=`getent passwd $user | cut -d: -f6`
        export XAUTHORITY=$userhome/.Xauthority
        export username=$user
      else
        export XAUTHORITY=""
      fi
    }

    getXconsole() {
      console=`fgconsole`;
      displaynum=`ps t tty$console | sed -n -re 's,.*/X .*:([0-9]+).*,\1,p'`
      if [ x"$displaynum" != x"" ]; then
        export DISPLAY=":$displaynum"
        getXuser
      fi
    }


    # from acpi scripts: /usr/share/acpi-support/power-funcs
    getXconsole

    case "${1}" in
      suspend|hibernate)
        logger -p info "Suspend Script: lock screen!"
        if [ x"$username" != x"" ]; then
          su $username -c '/usr/bin/i3lock -ti ~/.local/share/wallpaper.png'
        fi
      ;;

      resume|thaw)
      ;;
    esac

    exit 0
