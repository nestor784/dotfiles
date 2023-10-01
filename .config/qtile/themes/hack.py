from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy



class Hack():
    groups_labels =  ['0123',[' M',' 1',' 2',' 3',]]
    colors = {
            "b_focus":["#7d85a8","#7d85a8"],
            "b_normal":["#0e101a","#0e101a"],
            "0":["#0e101a", "#0e101a"],
            "1":["#0e101a", "#0e101a"],
            "2":["#eceef3", "#eceef3"],
            "3":["#ea8538", "#ea8538"],
            "4":["#84e45b", "#84e45b"],
            "5":["#841620", "#841620"],
            }

    def sep(self):
        return widget.Sep(size_percent = 60,
                          margin = 5,
                          linewidth = 2,
                          background = self.colors["1"],
                          foreground = "#1c2034",
                          )
    def nerd_icon(self,nerdfont_icon,fg_color):
        return widget.TextBox(
                font = 'Iosevka Nerd Font',
                fontsize = 15,
                text = nerdfont_icon,
                foreground = fg_color,
                background = self.colors["1"],
                )

    def spacer(self):
        return widget.Spacer(
                length = 5,
                background = self.colors["1"],
                )

    @staticmethod
    def widget_defaults():
        return dict(
                font="Iosevka Nerd Font",
                fontsize=12,
                padding=5,
                )


    def init_widgets_list(self):
        widgets_list = [
                self.spacer(),
                widget.GroupBox(
                    fontsize=12,
                    foreground = self.colors["2"],
                    background = self.colors["1"],
                    borderwidth = 4,
                    highlight_method = "text",
                    this_current_screen_border = self.colors["4"],
                    active = self.colors["3"],
                    inactive = self.colors["2"],
                    disable_drag = True,
                    urgent_alert_method = 'text',
                    ),
                self.sep(),
                self.nerd_icon(' ', self.colors["5"]),
                widget.Battery(
                    low_foreground=self.colors["3"],
                    low_percentage=0.2,
                    format='{percent:.0%}',
                    font='Hack Nerd Font',
                    foreground=self.colors["2"],
                    background=self.colors["1"],
                    ),
                widget.Spacer(length=bar.STRETCH,background=self.colors["1"]),
                self.nerd_icon('󰃭 ',self.colors["5"]),
                widget.Clock(
                    fmt="{}",
                    format="%d %B %Y",
                    foreground=self.colors["2"],
                    background=self.colors["1"],
                    ),
                self.sep(),
                self.nerd_icon('󰞷',self.colors["5"]),
                widget.Prompt(
                    fmt="{}",
                    prompt="",
                    foreground = self.colors["3"],
                    background = self.colors["1"],
                    fontsize=14,
                    ),
                self.sep(),
                self.nerd_icon(' ',self.colors["5"]),
                widget.Clock(
                    fmt="{}",
                    format="%I:%M %p",
                    foreground=self.colors["2"],
                    background=self.colors["1"],
                    ),
                widget.Spacer(length=bar.STRETCH,background=self.colors["1"]),
                self.nerd_icon(' ',self.colors["5"]),
                widget.Net(
                    format = "{down}↓↑{up}",
                    foreground = self.colors["2"],
                    background = self.colors["1"],
                    update_interval = 3,
                    mouse_callbacks = {
                        'Button1':lambda : qtile.cmd_spawn("networkmanager_dmenu")
                        }
                    ),
                self.sep(),
                self.nerd_icon('󰓃',self.colors["5"]),
                widget.PulseVolume(
                    fmt='{}',
                    limit_max_volume=True,
                    foreground=self.colors["2"],
                    background=self.colors["1"],
                    ),
                widget.Systray(
                    background=self.colors["1"],
                        ),
                self.spacer(),
                widget.QuickExit(),
                ]
        return widgets_list

    def init_screens(self):
        wallpaper_folder = '~/.config/qtile/wallpapers/'
        options = {
                'size' : 35,
                'opacity' : 0.9,
                'margin':[5,10,0,10],
                }
        options2 = {
                'wallpaper': wallpaper_folder+'kotonoha_no_niwa.jpg',
                'wallpaper_mode':'fill',
                }

        return [Screen(top=bar.Bar(widgets=self.init_widgets_list(),**options),**options2)]

