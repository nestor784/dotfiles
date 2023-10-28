import os
from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget as extrawidget
from qtile_extras import bar as extrabar
from qtile_extras.widget.decorations import RectDecoration



class Theme():
    name = "Nice"
    groups =  ['12345',[' ','󰊢 ',' ',' ',' ']]
    colors = {
            "b_focus":["#f7b1bb","#f7b1bb"],
            "b_normal":["#f4e7fc","#f4e7fc"],
            "1":"#d29ef2",
            "2":"#f4e7fc",
            "3":"#ff9b66",
            "4":"#eb8997",
            "5":"#c3f7f5",
            "6":"#99ea99",
            "7":"#efe97e",
            "8":"#f7b1bb",
            "9":"#09000f",
            "10":"#73677c",
            "11":"#94cfe0",
            "12":"#310651",
            "13":"#dacee3",
            }
    
    @lazy.function
    def nextwallpaper(self):
        os.system("exec feh --bg-fill --randomize ~/.config/qtile/themes/nice/wallpapers/*")

    def init_groups(self):
        return [Group(i,label=k) for i,k in zip(self.groups[0],self.groups[1])]
   
    @staticmethod
    def decor(color,radius):
        return {
                "decorations":[
                    RectDecoration(colour=color,radius=radius,filled=True,padding_y=4, group=True),
                    ],
                }

    def sep(self):
        return widget.TextBox(
                text = "󰇙",
                foreground = self.colors["2"],
                fontsize = 18,
                padding = 5,
                )

    def nerd_icon(self,icon,fg,callback={},options={}):
        return extrawidget.TextBox(
                text = icon,
                foreground = fg,
                fontsize = 16,
                padding=10,
                mouse_callbacks=callback,
                **options,
                )

    @staticmethod
    def widget_defaults():
        return dict(

                font="JetBrainsMono Nerd Font",
                fontsize=13,
                padding=0,
                )
    
    def spacer(self,fg,bg,d=True):
        mydecor = self.decor(bg,0)
        if d:
            t = ""
        else:
            t = ""
        return extrawidget.TextBox(
                text = t,
                fontsize=13,
                foreground = fg,
                **mydecor
                )
    
    def sepblank(self):
        return widget.Sep(size_percent = 60,
                          margin = 5,
                          linewidth = 4,
                          background = self.colors["12"],
                          foreground = self.colors["12"],
                          )


    def init_widgets_list(self):
        groupboxdecor = self.decor(self.colors["11"],9)
        volumedecor = self.decor(self.colors["8"],[9,0,0,9])
        wlandecor = self.decor(self.colors["6"],[0,9,9,0])
        batterydecor = self.decor(self.colors["7"],0)
        memorydecor = self.decor(self.colors["11"],[9,0,0,9])
        spacedecor = self.decor(self.colors["4"],[0,9,9,0])
        clockdecor = self.decor(self.colors["3"],9)
        wnamedecor = self.decor(self.colors["12"],9)
        archico = {
                'icon':" 󰣇 ",
                'fg':self.colors["9"],
                'callback':{'Button1': self.nextwallpaper,},
                'options':self.decor(self.colors["1"],9),
                }
        widgets_list = [
                self.sepblank(),
                self.nerd_icon(**archico),
                self.sep(),
                extrawidget.GroupBox(
                    foreground = self.colors["9"],
                    borderwidth = 4,
                    highlight_method = "text",
                    this_current_screen_border = self.colors["2"],
                    active = self.colors["9"],
                    inactive = self.colors["9"],
                    disable_drag = True,
                    urgent_alert_method = 'text',
                    urgent_text = self.colors["9"],
                    **groupboxdecor,
                    ),
                self.sep(),
                extrawidget.PulseVolume(
                    fmt='󰕾 {}',
                    padding=10,
                    limit_max_volume=True,
                    foreground=self.colors["9"],
                    **volumedecor,
                    ),
                self.spacer(fg=self.colors["8"],bg=self.colors["4"]),
                extrawidget.DF(
                    format="󰆼 {r:.0f}%",
                    partition="/home",
                    visible_on_warn=False,
                    foreground=self.colors["9"],
                    padding=10,
                    **spacedecor,
                    ),
                widget.Spacer(length=bar.STRETCH),
                extrawidget.WindowName(
                    foreground = self.colors["13"],
                    fmt = "{}",
                    empty_group_string="nestor",
                    scroll=True,
                    width= 400,
                    padding = 20,
                    scroll_delay=1,
                    scroll_interval=0.05,
                    scroll_step=2,
                    **wnamedecor,
                    ),
                widget.Spacer(length=bar.STRETCH),
                extrawidget.Memory(
                    format="󰍛 {MemPercent}",
                    foreground=self.colors["9"],
                    **memorydecor,
                    padding=10,
                    ),
                self.spacer(fg=self.colors["11"],bg=self.colors["7"]),
                extrawidget.Battery(
                    format='{char} {percent:.0%} ',
                    foreground=self.colors["9"],
                    notify_below=20,
                    notification_timeout=0,
                    full_char=' ',
                    charge_char=" ",
                    discharge_char=" ",
                    empty_char=" ",
                    update_interval=2,
                    show_short_text=False,
                    **batterydecor,
                    padding=5,
                    ),
                self.spacer(fg=self.colors["6"],bg=self.colors["7"],d=False),
                extrawidget.Wlan(
                    format = " {percent:2.0%}",
                    padding = 10,
                    foreground = self.colors["9"],
                    interface="wlp2s0",
                    disconnected_message="󰖪 0%",
                    update_interval = 1,
                    mouse_callbacks = {
                        'Button1':lambda : qtile.cmd_spawn("networkmanager_dmenu")
                        },
                    **wlandecor,
                    ),
                self.sep(),
                extrawidget.Clock(
                    fmt="{}",
                    format=" %b %d %Y | %I:%M %p",
                    foreground=self.colors["9"],
                    padding=12,
                    **clockdecor,
                    ),
                widget.Systray(
                        icon_size=20,
                        padding=10,
                        ),
                self.sepblank(),
                ]
        return widgets_list

    def init_screens(self):
        options = {
                'size' : 25,
                'background' : self.colors['12'],
                'opacity' : 1,
                'margin':[5,7,0,7], 
                }
        return [Screen(top=extrabar.Bar(widgets=self.init_widgets_list(),**options))]
