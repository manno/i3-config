# i3-config

Disclaimer.

## Installation

    apt-get install libpulse-dev nitrogen i3 i3lock i3status

### Wallpaper    

Expected at `~/.local/share/wallpaper.png`.

### Volume Control

https://github.com/falconindy/ponymix

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
