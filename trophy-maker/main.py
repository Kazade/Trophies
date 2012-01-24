#!/usr/bin/env python

import sys
import uuid
from gi.repository import Gtk

class MainWindow(object):
    LABEL_WIDTH = 100

    def __init__(self, *args, **kwargs):    
        self._window = Gtk.Window()
        self._window.connect("destroy", self.on_window_close)
        
        self._construct_form()
        
        self._window.set_title("Trophy Maker")
        self._window.show_all()


    def _construct_id_row(self):
        self._id_label = Gtk.Label("ID")
        self._id_label.set_size_request(self.LABEL_WIDTH, -1)
        self._id_label.set_alignment(1.0, 0.5)
        
        self._id_value = Gtk.Entry()
        self._id_value.set_text(uuid.uuid1().hex)
        self._id_value.set_sensitive(False)

        self._id_box = Gtk.HBox()
        self._id_box.pack_start(self._id_label, False, False, 5)
        self._id_box.pack_start(self._id_value, False, False, 5)
        
        return self._id_box

    def _construct_name_row(self):
        self._name_label = Gtk.Label("Name")
        self._name_label.set_size_request(self.LABEL_WIDTH, -1)
        self._name_label.set_alignment(1.0, 0.5)        
        self._name_value = Gtk.Entry()
        self._name_box = Gtk.HBox()
        self._name_box.pack_start(self._name_label, False, False, 5)
        self._name_box.pack_start(self._name_value, False, False, 5)
        
        return self._name_box

    def _construct_form(self):
        self._vbox = Gtk.VBox()
        self._vbox.pack_start(self._construct_id_row(), False, False, 5)
        self._vbox.pack_start(self._construct_name_row(), False, False, 5)        
        
        self._window.add(self._vbox)

    def on_window_close(self, window):
        Gtk.main_quit()

def main():
    window = MainWindow()
    Gtk.main()

    return 0

if __name__ == '__main__':
    sys.exit(main())
