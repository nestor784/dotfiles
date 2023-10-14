import os
from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget as extrawidget
from qtile_extras import bar as extrabar
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration



class Theme():
    name = "Hack"
    groups =  ['12345',[' ','󰊢 ',' ',' ',' ']]
    colors = {
            "b_focus":"#2A2940",
            "b_normal":"#310A31",
            "bar":"#DCD6F7",
            "archico":"#A6B1E1",
            "groupbox":"#2A2940",
            "windowname":"#310A31",
            "volume":"#1D1128",
            "disk":"#e5d4ed",
            "ram":"#847996",
            "battery":"#B4869F",
            "wifi":"#985F6F",
            "date":"#4E4C67",
            }

    @lazy.function
    def nextwallpaper(self):
        os.system("exec feh --bg-fill --randomize ~/.config/qtile/themes/hack/wallpapers/*")

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
                foreground="#FFFFFF",
                )
    
    def init_widgets_list(self):
        widgets_list = [
                extrawidget.TextBox(
                    foreground = self.colors["windowname"],
                    text ="󰣇",
                    padding = 15,
                    background = self.colors["archico"],
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 18,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('kitty'),},
                    **self.powerline({}),
                    ),
                extrawidget.CurrentLayoutIcon(
                    background = self.colors["groupbox"],
                    fmt ="",
                    padding = 5,
                    scale = 0.6,
                    ),
                extrawidget.GroupBox(
                    background = self.colors["groupbox"],
                    highlight_color = self.colors["groupbox"],
                    borderwidth = 2,
                    highlight_method = "line",
                    this_current_screen_border = "#973450",
                    margin_y = 2,
                    active = "#C6C4D0",
                    inactive = "#FFFFFF",
                    disable_drag = True,
                    urgent_alert_method = 'line',
                    urgent_text = "#791415",
                    **self.powerline({}),
                    ),
                widget.Spacer(length=bar.STRETCH,background=self.colors["bar"],),
                extrawidget.WindowName(
                    background = self.colors["bar"],
                    foreground = self.colors["windowname"],
                    fmt = "{}",
                    empty_group_string="nestor",
                    ),
                extrawidget.Spacer(length=bar.STRETCH,background=self.colors["bar"],**self.powerline({"path":"rounded_right"}),),
                extrawidget.PulseVolume(
                    background = self.colors["volume"],
                    fmt='󰕾 {}',
                    limit_max_volume=True,
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.DF(
                    foreground = self.colors["windowname"],
                    background = self.colors["disk"],
                    format="󰆼 {r:.0f}%",
                    partition="/home",
                    visible_on_warn=False,
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.Memory(
                    foreground = self.colors["windowname"],
                    background = self.colors["ram"],
                    format="󰍛 {MemPercent}",
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.Battery(
                    background = self.colors["battery"],
                    format='{char} {percent:.0%}',
                    full_char='󰂂',
                    charge_char="󰂄",
                    discharge_char="󰁼",
                    empty_char="󰂎",
                    update_interval=2,
                    show_short_text=False,
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.Wlan(
                    background = self.colors["wifi"],
                    format = " {percent:2.0%}",
                    interface="wlp2s0",
                    disconnected_message="󰖪 0%",
                    update_interval = 1,
                    mouse_callbacks = {
                        'Button1':lambda : qtile.cmd_spawn("networkmanager_dmenu")
                        },
                    **self.powerline({"path":"forward_slash",}),
                    ),
                extrawidget.Clock(
                    background = self.colors["date"],
                    fmt="{}",
                    format=" %b %d %Y %I:%M %p",
                    **self.powerline({"path":"forward_slash",}),
                    ),
                widget.Systray(
                        icon_size = 14,
                        background = self.colors["volume"]
                        ),
                extrawidget.TextBox(
                    text ="󰒭",
                    padding = 5,
                    background = self.colors["volume"],
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 15,
                    mouse_callbacks = {'Button1':   self.nextwallpaper,},
                    ),
                ]
        return widgets_list

    def init_screens(self):
        options = {
                'size' : 22,
                'background' : self.colors["bar"]+".0",
                'opacity' : 1,
                'margin': [0,40,0,40], 
                }
        return [Screen(top=bar.Bar(widgets=self.init_widgets_list(),**options))]
