import os
import subprocess
from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget as extrawidget
from qtile_extras import bar as extrabar
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration



class Theme():
    name = "ghibli"
    groups =  ['123',['','','']]
    colors = {
            "b_focus":"#61677A",
            "b_normal":"#272829",
            "base":"#272829",
            "light":"#D8D9DA",
            "gray":"#61677A",
            "cream":"#FFF6E0",
            "dark":"#040404",
            "night":"#171819",
            }

    @lazy.function
    def nextwallpaper(self):
        os.system("exec feh --bg-fill --randomize ~/.config/qtile/themes/ghibli/wallpapers/*")

    @lazy.function
    def show_memory_usage(self):
        run = os.path.expanduser("~/.config/qtile/scripts/showmemoryusage.sh")
        subprocess.call([run])

    @lazy.function
    def show_disk_usage(self):
        run = os.path.expanduser("~/.config/qtile/scripts/showdiskusage.sh")
        subprocess.call([run])

    @lazy.function
    def show_battery(self):
        run = os.path.expanduser("~/.config/qtile/scripts/showbattery.sh")
        subprocess.call([run])

    @lazy.function
    def show_calendar(self,arg):
        run = os.path.expanduser("~/.config/qtile/scripts/calendar.sh")
        subprocess.call([run,arg])

    def init_groups(self):
        return [Group(i,label=k) for i,k in zip(self.groups[0],self.groups[1])]

    @staticmethod
    def powerline(path):
        return {
                "decorations":[
                    PowerLineDecoration(size=13,**path),
                    ],
                }

    @staticmethod
    def widget_defaults():
        return dict(
                font="JetBrainsMono Nerd Font",
                fontsize=12,
                padding=0,
                foreground="#D8D9DA",
                background="#040404"
                )
    
    def init_widgets_list(self):
        widgets_list = [
                extrawidget.TextBox(
                    foreground = self.colors["cream"],
                    text ="󰣇",
                    padding = 10,
                    background = self.colors["base"],
                    fontsize = 14,
                    mouse_callbacks = {'Button1': self.nextwallpaper,},
                    **self.powerline({"path":"back_slash"}),
                    ),
                extrawidget.CurrentLayoutIcon(
                    background = "#101010",
                    fmt ="",
                    scale = 0.6,
                    **self.powerline({"path":"back_slash"}),
                    ),
                extrawidget.GroupBox(
                    background = "#080808",
                    highlight_color = self.colors["base"],
                    borderwidth = 2,
                    highlight_method = "text",
                    this_current_screen_border = self.colors["cream"],
                    margin_y = 2,
                    active = self.colors["base"],
                    inactive = self.colors["base"],
                    disable_drag = True,
                    urgent_alert_method = 'text',
                    urgent_text = self.colors["base"],
                    **self.powerline({"path":"back_slash"}),
                    ),
                widget.Spacer(length=bar.STRETCH),
                extrawidget.WindowName(
                    fmt = "{}",
                    empty_group_string="nestor",
                    ),
                extrawidget.Spacer(
                    length=bar.STRETCH,
                    **self.powerline({"path":"forward_slash"}),
                    ),
                #extrawidget.PulseVolume(
                #    fmt = '{}',
                #    background = self.colors["night"], 
                #    emoji = True,
                #    emoji_list = ["󰝟","󰕿","󰖀","󰕾"],
                #    limit_max_volume=True,
                #    **self.powerline({"path":"forward_slash",}),
                #    ),
                extrawidget.Battery(
                    background = "#141415",
                    format='{char}',
                    full_char='󰂂',
                    notify_below=20,
                    notification_timeout=0,
                    charge_char="󰂄",
                    discharge_char="󰁼",
                    empty_char="󰂎",
                    update_interval=2,
                    show_short_text=False,
                    mouse_callbacks={'Button1': self.show_battery,},
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.Wlan(
                    background = "#101010",
                    format = " ",
                    interface="wlp2s0",
                    disconnected_message="󰖪 ",
                    update_interval = 1,
                    mouse_callbacks = {
                        'Button1':lambda : qtile.cmd_spawn("networkmanager_dmenu")
                        },
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.TextBox(
                    background = "#080808",
                    text="󰆼",
                    mouse_callbacks = {'Button1': self.show_disk_usage,},
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.TextBox(
                    background = "#040404",
                    text="󰍛",
                    mouse_callbacks = {'Button1': self.show_memory_usage,},
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.TextBox(
                    background = "#000000",
                    text=" ",
                    mouse_callbacks = {
                        'Button1': self.show_calendar("prev"),
                        'Button2': self.show_calendar("curr"),
                        'Button3': self.show_calendar("next"),
                        },
                    ),
                widget.Systray(
                        icon_size = 13,
                        ),
                ]
        return widgets_list

    def init_screens(self):
        options = {
                'size' : 20,
                'background' : self.colors["dark"],
                'opacity' : 0.7,
                'margin': 0, 
                }
        return [Screen(
            top=bar.Bar(widgets=self.init_widgets_list(),**options),
            )]
