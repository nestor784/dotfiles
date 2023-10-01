from libqtile import layout, qtile
from libqtile.config import Group, Key
from libqtile.lazy import lazy

mod = "mod4"

def init_groups(groups):
    return [Group(i,label=k) for i,k in zip(groups[0],groups[1])]

def init_keyextend(i):
    return [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]


def init_layout_theme(theme):
    return {
            "border_width":4,
            "margin":15,
            "border_focus":theme.colors["b_focus"],
            "border_normal":theme.colors["b_normal"],
            }

def init_layouts(layout_theme):
    return [
            layout.MonadTall(**layout_theme),
            layout.Stack(num_stacks=2,**layout_theme),
            layout.Tile(**layout_theme),
            layout.Max(**layout_theme),
            ]
