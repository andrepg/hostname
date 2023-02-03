from gi.repository import Gio
from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/io/github/andrepg/hostname/window.ui')
class HostnameWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'HostnameWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Bind settings of application with Settings database
        self.settings = Gio.Settings(schema_id='io.github.andrepg.hostname')
        self.settings.bind("window-width", self, "default-width", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("window-height", self, "default-height", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("is-maximized", self, "maximized", Gio.SettingsBindFlags.DEFAULT)
