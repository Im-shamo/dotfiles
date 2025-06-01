from libqtile import layout

from configuration.variables import *

layouts = [
        layout.Bsp(
        margin = margin, 
        margin_on_single = margin, 
        border_focus = border_focus_colour,
        border_normal = border_normal_colour, 
        border_on_single = True,
        border_width = border_width,
    ),
    layout.Max(
        margin = margin,
        border_focus = border_focus_colour,
        border_normal = border_normal_colour,
        border_width = border_width,
    ),
]