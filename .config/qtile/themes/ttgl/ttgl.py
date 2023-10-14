from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy



class Theme():
    name = "Ttgl"
    groups =  ['12345',[' ',' ',' ','󰝚 ',' ']]
    colors = {
            "b_focus":["#C88740","#C88740"],
            "b_normal":["#140F15","#140F15"],
            "1":["#140F15", "#140F15"],
            "2":["#C68526", "#C68526"],
            "3":["#A12807", "#A12807"],
            "4":["#F0D5B6", "#F0D5B6"],
            "5":["#FFAD00", "#FFAD00"],
            "6":["#DBA96D", "#DBA96D"],
            "7":["#3F231E","#3F231E"],
            "8":["#E4D0CB","#E4D0CB"],
            }
    
    @lazy.function
    def nextwallpaper(self):
        os.system("exec feh --bg-fill --randomize ~/.config/qtile/themes/ttgl/wallpapers/*")

    def init_groups(self):
        return [Group(i,label=k) for i,k in zip(self.groups[0],self.groups[1])]

    def sep(self):
        return widget.TextBox(
                fontsize = 15,
                text = " 󰇙 ",
                foreground = self.colors["2"],
                background = self.colors["1"],
                )

    def nerd_icon(self,icon,fg,bg,size=15,callback={}):
        return widget.TextBox(
                fontsize = size,
                text = icon,
                foreground = fg,
                background = bg,
                padding=0,
                mouse_callbacks=callback,
                )

    def spacer(self,fg,bg, d=True):
        if d:
            t = " "
        else:
            t = " "
        return widget.TextBox(
                fontsize = 22,
                text = t,
                foreground = fg,
                background = bg,
                padding=-1,
                )

    @staticmethod
    def widget_defaults():
        return dict(
                font="Hurmit Nerd Font",
                fontsize=12,
                padding=0,
                )


    def init_widgets_list(self):
        archico = {
                'icon':" 󰣇 ",
                'fg':self.colors["8"],
                'bg':self.colors["7"],
                'callback':{'Button1': self.nextwallpaper,}
                }
        widgets_list = [
                self.nerd_icon(**archico),
                self.spacer(fg=self.colors["7"],bg=self.colors["3"]),
                widget.Battery(
                    format='{char} {percent:.0%} ',
                    foreground=self.colors["1"],
                    background=self.colors["3"],
                    full_char=' ',
                    charge_char=" ",
                    discharge_char=" ",
                    empty_char=" ",
                    update_interval=2,
                    show_short_text=False,
                    ),
                self.spacer(fg=self.colors["3"],bg=self.colors["5"]),
                widget.Clock(
                    fmt="{}",
                    format="%d %B %Y 󰇙 %I:%M %p",
                    foreground=self.colors["1"],
                    background=self.colors["5"],
                    ),
                self.spacer(fg=self.colors["5"],bg=self.colors["1"]),
                widget.Spacer(length=bar.STRETCH,background=self.colors["1"]),
                widget.GroupBox(
                    fontsize=15,
                    foreground = self.colors["2"],
                    background = self.colors["1"],
                    borderwidth = 4,
                    highlight_method = "text",
                    this_current_screen_border = self.colors["6"],
                    active = self.colors["2"],
                    inactive = self.colors["2"],
                    disable_drag = True,
                    urgent_alert_method = 'text',
                    urgent_text = self.colors["3"]
                    ),
                widget.Spacer(length=bar.STRETCH,background=self.colors["1"]),
                self.spacer(fg=self.colors["4"],bg=self.colors["1"],d=False),
                widget.WindowName(
                    background = self.colors["4"],
                    foreground = self.colors["1"],
                    fmt = "  {}",
                    empty_group_string="nestor",
                    scroll=True,
                    width= 80,
                    scroll_delay=1,
                    scroll_interval=0.05,
                    scroll_step=2,
                    ),
                self.spacer(fg=self.colors["6"],bg=self.colors["4"],d=False),
                widget.Net(
                    format = " {up}{down}",
                    foreground = self.colors["1"],
                    background = self.colors["6"],
                    update_interval = 3,
                    mouse_callbacks = {
                        'Button1':lambda : qtile.cmd_spawn("networkmanager_dmenu")
                        }
                    ),
                self.spacer(fg=self.colors["2"],bg=self.colors["6"],d=False),
                widget.PulseVolume(
                    fmt='󰕾 {}  ',
                    limit_max_volume=True,
                    foreground=self.colors["1"],
                    background=self.colors["2"],
                    ),
                widget.Systray(
                        icon_size=20,
                        background=self.colors["2"],
                        ),
                ]
        return widgets_list

    def init_screens(self):
        options = {
                'size' : 22,
                'opacity' : 1,
                'margin':[0,0,0,0],
                }
        return [Screen(top=bar.Bar(widgets=self.init_widgets_list(),**options))]
