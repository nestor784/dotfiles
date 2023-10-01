import os
from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


from themes.pyq.keybindings import keymappings
from themes.pyq.gl import init_groups, init_keyextend, init_layout_theme, init_layouts
from themes.pyq.oscommands import init_oscommands
from themes.selectedtheme import Theme

mod = "mod4"
terminal = "kitty"
theme = Theme()

keys = keymappings()
groups = init_groups(theme.groups_labels)
layout_theme = init_layout_theme(theme) 
layouts = init_layouts(layout_theme)
widget_defaults = theme.widget_defaults()
extension_defaults = theme.widget_defaults()
screens = theme.init_screens()



for i in groups:
    keys.extend(init_keyextend(i))

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
init_oscommands()
