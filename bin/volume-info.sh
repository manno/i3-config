echo -n "Master: "
pactl list sinks | perl -an -E 'say $F[2] if /^\s+Volume:/'
