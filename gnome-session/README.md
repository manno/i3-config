# Added Session Files
 
# Modified Autostarts

# Start GNOME Keyring

`.bashrc`:

  if [ -n "$PS1" ]; then
    eval `/usr/bin/gnome-keyring-daemon -s`
    export SSH_AUTH_SOCK
    export GPG_AGENT_INFO
  fi

# Probably don't need this?

`.xinitrc`

  # Start GNOME Keyring
  eval $(/usr/bin/gnome-keyring-daemon --start --components=gpg,pkcs11,secrets,ssh)
  # You probably need to do this too:
  export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK
