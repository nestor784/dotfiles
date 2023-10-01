import os
def init_oscommands():
    commands = [
            'exec picom --config $HOME/.config/qtile/picom.conf &',
            ]
    for command in commands:
        os.system(command)
