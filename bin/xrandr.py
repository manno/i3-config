#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os
import getpass

class actions:

    def key_press_action(self,widget,event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        if(keyname == 'Escape'):
          gtk.main_quit()

    def cancel_action(self,btn):
        gtk.main_quit()

    def xrandr_single_action(self,btn):
        self.status.set_label("running xrandr")
        os.system("xrandr --fb 1600x900 --output VGA1 --off --output HDMI3 --off --output DP-2 --off --output LVDS1 --auto")
        os.system("~/.config/i3/bin/compton reset")
        os.system("~/.config/i3/bin/awsetbg ~/.local/share/wallpaper.png")
        gtk.main_quit()

    def xrandr_home_action(self,btn):
        self.status.set_label("running xrandr")
        os.system("xrandr --output LVDS1 --auto --output HDMI3 --auto --left-of LVDS1")
        os.system("~/.config/i3/bin/compton reset")
        os.system("~/.config/i3/bin/awsetbg ~/.local/share/wallpaper.png")
        gtk.main_quit()

    def add_button(self, title, action):
        button = gtk.Button(title)
        button.set_border_width(4)
        button.connect("clicked", action)
        self.button_box.pack_start(button)
        button.show()

    def create_window(self):
        self.window = gtk.Window()
        title = "Choose an option:"
        self.window.set_title(title)
        self.window.set_border_width(5)
        self.window.set_size_request(500, 80)
        self.window.set_resizable(False)
        self.window.set_keep_above(True)
        self.window.stick
        self.window.set_position(1)
        self.window.connect("delete_event", self.cancel_action)
        windowicon = self.window.render_icon(gtk.STOCK_QUIT, gtk.ICON_SIZE_MENU)
        self.window.set_icon(windowicon)

        #Create HBox for buttons
        self.button_box = gtk.HBox()
        self.button_box.show()
        
        # Actions
        self.add_button("_Single", self.xrandr_single_action)
        self.add_button("_Home", self.xrandr_home_action)

        #Cancel button
        self.cancel = gtk.Button(stock = gtk.STOCK_CANCEL)
        self.cancel.set_border_width(4)
        self.cancel.connect("clicked", self.cancel_action)
        self.button_box.pack_start(self.cancel)
        self.cancel.show()
        
        #Create HBox for status label
        self.label_box = gtk.HBox()
        self.label_box.show()
        self.status = gtk.Label()
        self.status.show()
        self.label_box.pack_start(self.status)
        
        #Create VBox and pack the above HBox's
        self.vbox = gtk.VBox()
        self.vbox.pack_start(self.button_box)
        self.vbox.pack_start(self.label_box)
        self.vbox.show()

        #Escape key quits
        self.window.connect("key_press_event", self.key_press_action)
        
        self.window.add(self.vbox)
        self.window.show()
        
    def __init__(self):
        self.actions = []
        self.create_window()
        os.system("~/.config/i3/bin/keymap")


def main():
    gtk.main()

if __name__ == "__main__":
    go = actions()
    main()
