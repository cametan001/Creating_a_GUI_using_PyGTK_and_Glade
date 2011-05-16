#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import os, os.path, sys, pygtk, gtk

class HelloWorldGTK:
    """This is an Hello World GTK application"""

    def __init__(self):

        # Set the Glade file
        self.gladefile = "PyHelloWorld.ui"
        self.wTree = gtk.Builder()
        self.wTree.add_from_file(os.path.join(os.path.dirname(__file__), self.gladefile))
        # Create our dictionary and connect it
        dic = {
            "on_btnHelloWorld_clicked" : self.btnHelloWorld_clicked,
            "on_MainWindow_destroy" : gtk.main_quit
            }
        self.wTree.connect_signals(dic)

        # Get the Main Window, and connect the "destroy" event
        self.window = self.wTree.get_object("MainWindow")
        self.window.show_all()

    def btnHelloWorld_clicked(self, widget):
        print "Hello World!"

if __name__ == '__main__':
    hwg = HelloWorldGTK()
    gtk.main()
