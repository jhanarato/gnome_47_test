# window.py
#
# Copyright 2024 Ajahn Jhanarato
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/org/bswa/Gnome47Test/window.ui')
class Gnome47TestWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'Gnome47TestWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'gnome_47_test'
        self.props.version = "0.1.0"
        self.props.authors = ['Ajahn Jhanarato']
        self.props.copyright = '2022 Ajahn Jhanarato'
        self.props.logo_icon_name = 'org.bswa.Gnome47Test'
        self.props.modal = True
        self.set_transient_for(parent)
