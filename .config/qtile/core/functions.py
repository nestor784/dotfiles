import os
from libqtile.lazy import lazy

## Lazy functions
@lazy.function
def run_rofi(qtile):
    os.system("exec ~/.config/rofi/scripts/launcher_t4")

@lazy.function
def run_powermenu(qtile):
    os.system("exec ~/.config/rofi/scripts/powermenu_t1")

@lazy.function
def takescreenshot(qtile):
    os.system("import -window root .screenshots/$(date +%Y-%m-%d_%T).jpg")

@lazy.function
def run_theme_manager(qtile):
    os.system("exec ~/.config/qtile/scripts/theme_selector")

@lazy.function
def up_brightness(qtile):
    os.system("exec brightnessctl set +10%")

@lazy.function
def down_brightness(qtile):
    os.system("exec brightnessctl set 10%-")

@lazy.function
def change_xkb_layout(qtile):
    os.system("exec ~/.config/qtile/scripts/chlanguage.sh")
