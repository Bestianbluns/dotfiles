from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

    # Change window sizes (Bsp and ModalTall)
    Key([mod, "control"], "Up", 
        lazy.layout.grow_up(),
        lazy.layout.grow()
        ),
    Key([mod, "control"], "Down", 
        lazy.layout.grow_down(),
        lazy.layout.shrink()
        ),
    Key([mod, "control"], "Left", lazy.layout.grow_left()),
    Key([mod, "control"], "Right", lazy.layout.grow_right()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    # Flip
    Key([mod], "p", lazy.layout.flip()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),

    # Kill window
    Key([mod], "w", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    #Key([mod], "r", lazy.spawncmd()),
    Key([mod], "space", lazy.window.toggle_floating()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # ------------ App Configs ------------

    # Menu
    Key([mod], "m",
        lazy.spawn(".config/rofi/launchers/colorful/launcher.sh")
    ),

    # Bar
    Key([mod], "b", lazy.hide_show_bar("all")),

    # File Explorer
    Key([mod], "e", lazy.spawn("thunar")),

    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Screenshots - Scrot
    Key([mod], "s", lazy.spawn("scrot Screenshots/%b%d::%H%M%S.png -u")),
    Key([mod, "shift"], "s", lazy.spawn("scrot Screenshots/%b%d::%H%M%S.png -s")),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]
