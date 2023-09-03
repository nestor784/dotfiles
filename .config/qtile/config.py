# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty" # guess_terminal()

@lazy.function
def run_rofi(qtile):
    os.system("rofi -show drun")

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "s" , run_rofi , desc="Launch rofi"),
    # Dmenu
    #Key([mod], "s", 
    #    lazy.run_extension(extension.DmenuRun(
    #            dmenu_prompt=">_",
    #            dmenu_command="dmenu_run",
    #            dmenu_font="Andika-8",
    #            background="#232842",
    #            foreground="#eceef3",
    #            selected_background="#232842",
    #            selected_foreground="#1bd08a",
    #            dmenu_lines=15,
    #            dmenu_height=10,
    #        ) 
    #    ), 
    #    desc="Launch dmenu"),
    #
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([],"XF86AudioRaiseVolume",lazy.widget["pulsevolume"].increase_vol(), desc="Increase volume"),
    Key([],"XF86AudioLowerVolume",lazy.widget["pulsevolume"].decrease_vol(), desc="Decrease volume"),
]

groups = [Group(i,label=k) for i,k in zip('0123',[' M',' 1',' 2',' 3',])]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
        "border_width":4,
        "margin":15,
        "border_focus":"#7d85a8",
        "border_normal":"#0e101a",
        }


layouts = [
    layout.MonadTall(**layout_theme),
    layout.Stack(num_stacks=2,**layout_theme),
    layout.Tile(**layout_theme),
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    #layout.Bsp(),
   # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

def init_colors():
    return [["#0e101a", "#0e101a"], # Dark blue
            ["#0e101a", "#0e101a"],
            ["#eceef3", "#eceef3"], # White
            ["#ea8538", "#ea8538"], # Orange
            ["#84e45b", "#84e45b"], # Green
            ["#2861d4", "#2861d4"], # Blue cyan
            ]

def init_separator():
    return widget.Sep(
            size_percent = 60,
            margin = 5,
            linewidth = 2,
            background = colors[1],
            foreground = "#1c2034",
            )

def nerd_icon(nerdfont_icon,fg_color):
    return widget.TextBox(
            font = 'Iosevka Nerd Font',
            fontsize = 15,
            text = nerdfont_icon,
            foreground = fg_color,
            background = colors[1],
            )
def init_edge_spacer():
    return widget.Spacer(
            length = 5,
            background = colors[1],
            )

colors = init_colors()
sep = init_separator()
space = init_edge_spacer()


widget_defaults = dict(
    font="Iosevka Nerd Font",
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
            space,
            #widget.CurrentLayout(),
            widget.GroupBox(
                fontsize=12,
                foreground = colors[2],
                background = colors[1],
                borderwidth = 4,
                highlight_method = "text",
                this_current_screen_border = colors[4],
                active = colors[3],
                inactive = colors[2],
                ),
            sep,
            nerd_icon(' ',colors[5]),
            widget.Battery(
                low_foreground=colors[3],
                low_percentage=0.2,
                format='{percent:.0%}',
                font='Hack Nerd Font',
                foreground=colors[2],
                background=colors[1],
                ),
            widget.Spacer(length=bar.STRETCH,background=colors[1]),
            nerd_icon('󰃭 ',colors[5]),
            widget.Clock(
                fmt="{}",
                format="%d %B %Y",
                foreground=colors[2],
                background=colors[1],
                ),
            sep,
            nerd_icon('󰞷',colors[5]),
            widget.Prompt(
                fmt="{}",
                prompt="",
                foreground = colors[3],
                background = colors[1],
                fontsize=14,
                ),
            sep,
            nerd_icon(' ',colors[5]),
            widget.Clock(
                fmt="{}",
                format="%I:%M %p",
                foreground=colors[2],
                background=colors[1],
                ),
            widget.Spacer(length=bar.STRETCH,background=colors[1]),
            #widget.Prompt(),
            #widget.WindowName(),
            #widget.Chord(
            #    chords_colors={
            #        "launch": ("#ff0000", "#ffffff"),
            #    },
            #    name_transform=lambda name: name.upper(),
            #),
            # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
            # widget.StatusNotifier(),
            nerd_icon(' ',colors[5]),
            widget.Net(
                format = "{down}↓↑{up}",
                foreground = colors[2],
                background = colors[1],
                update_interval = 3,
                mouse_callbacks = {
                    'Button1':lambda : qtile.cmd_spawn("networkmanager_dmenu")
                    }
                ),
            sep,
            nerd_icon('󰓃',colors[5]),
            widget.PulseVolume(
                fmt='{}',
                limit_max_volume=True,
                foreground=colors[2],
                background=colors[1],
                ),
            widget.Systray(
                background=colors[1],
                    ),
            space,
            #widget.QuickExit(),
            ]
    return widgets_list

def init_screens():
    wallpaper_folder = '~/.config/qtile/wallpapers/'
    options = {
            'size' : 35,
            'opacity' : 0.9,
            'margin':[5,10,0,10],
            }
    wallpaper = {
            'wallpaper': wallpaper_folder + 'kotonoha_no_niwa.jpg',
            'wallpaper_mode':'fill',
            }
    return [Screen(top=bar.Bar(widgets=init_widgets_list(),**options),**wallpaper)]

screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

os_init_commands = [
        'exec picom --config $HOME/.config/qtile/picom.conf &',
        ] 

for command in os_init_commands:
    os.system(command)
