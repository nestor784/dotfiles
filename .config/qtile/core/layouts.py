from libqtile import layout, qtile
from libqtile.config import Group, Key
from libqtile.lazy import lazy

class Layouts:
    mod = "mod4"

    @staticmethod 
    def init_layout_theme(theme):
        return {
                "border_width":4,
                "margin":15,
                "border_focus":theme.colors["b_focus"],
                "border_normal":theme.colors["b_normal"],
                }

    @staticmethod
    def init_layouts(layout_theme):
        return [
                layout.MonadTall(**layout_theme),
                layout.Stack(num_stacks=2,**layout_theme),
                layout.Tile(**layout_theme),
                layout.Max(**layout_theme),
                ]
