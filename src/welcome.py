# window.py
#
# Copyright 2024 zoey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gio, GLib, Gtk, Pango

@Gtk.Template(resource_path='/org/zoey/Tabs/../data/ui/welcome.ui')
class TabsWelcome(Adw.ApplicationWindow):
    __gtype_name__ = 'TabsWindow'
    
    welcome_status = Gtk.Template.Child()

    ### Buttons ###
    download_tabs_button = Gtk.Template.Child()
    create_new_tab_button = Gtk.Template.Child()
    # Menu Button
    open_button = Gtk.Template.Child()

    ###Sidebar###
    split_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print("Welcome.py/TabsWelcome Loaded")
        #TODO - Open a MusicXML or JSON file using file picker.
        #Action that opens a file picker accepting either a JSON or MusicXML file to load into app.
        open_tab_action = Gio.SimpleAction(name="open")
        open_tab_action.connect("activate", self.open_tabs_file)
        self.add_action(open_tab_action)

        # TODO - Opens New window to download tabulatures from somewhere idk.
        download_tab_action = Gio.SimpleAction(name="download")
        download_tab_action.connect("activate", self.download_tab)
        self.add_action(download_tab_action)

        # TODO - Opens window to create a new blank tab
        create_tab_action = Gio.SimpleAction(name="create")
        create_tab_action.connect("activate", self.create_tabs_file)
        self.add_action(create_tab_action)

        # Hides sidebar button
        hide_sidebar_action = Gio.SimpleAction(name="hide_sidebar")
        hide_sidebar_action.connect("activate", self.toggle_sidebar)
        self.add_action(hide_sidebar_action)

    def download_tab(self, action, _):
        ''' Litteraly Just Prints Downloading For Now'''
        print("Downloading...")

    def open_tabs_file(self, action, _):
        """Litteraly Just Prints Meow"""
        print("Meow")

    def create_tabs_file(self, action, _):
        """Litteraly Just Prints Create Window"""
        print("Create Window")

    def toggle_sidebar(self, action, _):
        """ Reverses visibility status of sidebar"""
        toggle_status = self.split_view.get_show_sidebar()
        self.split_view.set_show_sidebar(not toggle_status)


