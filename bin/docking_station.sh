#!/bin/sh
# inspired of:                                                                                            
#   http://unix.stackexchange.com/questions/4489/a-tool-for-automatically-applying-randr-configuration-   when-external-display-is-p                                                                                
#   http://ozlabs.org/~jk/docs/mergefb/                                                                   
#   http://superuser.com/questions/181517/how-to-execute-a-command-whenever-a-file-changes/181543#181543  

export MONITOR2=/sys/class/drm/card0/card0-HDMI-A-3/status

while inotifywait -e modify,create,delete,open,close,close_write,access $MONITOR2;                        

dmode="$(cat $MONITOR2)"                                                                                  

do                                                                                                        
    if [ "${dmode}" = disconnected ]; then                                                                
         run-parts ~/.config/i3/xrandr/single
         echo "${dmode}"                                                                                  
    elif [ "${dmode}" = connected ];then                                                                  
         run-parts ~/.config/i3/xrandr/home
         echo "${dmode}"                                                                                  
    else /usr/bin/xrandr --auto                                                                           
         echo "${dmode}"                                                                                  
    fi                                                                                                    
done 
