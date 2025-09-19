from libqtile.lazy import lazy
import subprocess
import json

@lazy.function
def swap_screens(qtile):
    group_0 = qtile.screens[0].group
    group_1 = qtile.screens[1].group

    group_0.toscreen(screen=1)
    group_1.toscreen(screen=0)


def is_desktop():
    result = subprocess.run(["hostnamectl", "chassis"], capture_output = True, text=True)
    if result.stdout:
        return result.stdout[:-1] == "desktop"
    else:
        return False

def get_display_resolutions(qtile) -> dict[str, tuple[int, int]]:
    return {}
    output_dict = {}
    if qtile.core.name == "wayland":
        result = subprocess.run(["wlr-randr", "--json"], capture_output=True, text=True)
        if not result.stdout:
            return output_dict
        parsed = json.loads(result.stdout)
        for display in parsed:
            if not display["enable"]:
                continue
            for mode in display["modes"]:
                if mode["current"]:
                    output_dict[display["name"]] = (mode["width"], mode["height"])

    elif qtile.core.name == "x11":
        pass
    
    return output_dict