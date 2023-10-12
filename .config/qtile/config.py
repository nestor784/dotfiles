import os, subprocess
from libqtile import hook, bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from core.keys import Keys
from core.layouts import Layouts
from core.theme import Theme


mod = "mod4"
terminal = "kitty"

obj_keys = Keys()
obj_layouts = Layouts()
obj_theme  = Theme()

keys = obj_keys.keymappings()
groups = obj_theme.init_groups()
layout_theme = obj_layouts.init_layout_theme(obj_theme) 
layouts = obj_layouts.init_layouts(layout_theme)
widget_defaults = obj_theme.widget_defaults()
extension_defaults = obj_theme.widget_defaults()
screens = obj_theme.init_screens()



for i in groups:
    keys.extend(obj_keys.init_keyextend(i))

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "qtile" 

# Session init commands
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])
