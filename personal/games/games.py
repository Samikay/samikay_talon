import time

from typing import List
from talon import Module, Context, actions, ctrl, ui

mod = Module()

mod.mode("game", "Used to play games")
mod.tag("game_voip_muted", "Signals that game voice chat is muted")

self = actions.self

# You can use the default talon key_hold setting for generic presses, and this value + game_press_[key|mouse] for others.
setting_keymouse_delay = mod.setting(
    "game_keymouse_delay",
    type=float,
    default=0.05,
    desc="The length of time in seconds to hold a key/mouse button down for in game_press_[key|mouse]",
)

setting_game_window_size_x = mod.setting(
    "game_window_size_x",
    type=int,
    default=0,
    desc="When user.game_resize_window is called, this value is used",
)

setting_game_window_size_y = mod.setting(
    "game_window_size_y",
    type=int,
    default=0,
    desc="When user.game_resize_window is called, this value is used",
)

ctx = Context()
ctx.matches = r"""
mode: user.game
"""

ctx.settings = {
    #"speech.timeout": 0.05,
}


@mod.action_class
class Actions:
    # Game Mode
    def game_mode_enable():
        """Enable game mode"""
        actions.mode.disable("command")
        actions.mode.enable("user.game")
        update_tag(
            voip_muted(),
        )

    def game_mode_disable():
        """Disable game mode"""
        actions.mode.disable("user.game")
        actions.mode.enable("command")
        actions.user.mouse_release_held_buttons()

    def game_toggle_mute():
        """Toggle voice chat for game"""
        actions.user.abort_current_phrase()
        update_tag(
            actions.user.discord_toggle_mute(),
        )

    
    # Game Inputs
    def game_move_click(x: int, y: int, button: int = 0):
        """Moves mouse and clicks"""
        actions.user.mouse_move_relative_window(x, y)
        time.sleep(0.25) #give time for ui to respond
        self.game_press_mouse(button)
    
    def game_move_click_return(x: int, y: int):
        """Moves mouse, clicks, returns"""
        x_cur, y_cur = actions.user.mouse_position_relative_window()
        self.game_move_click(x, y)
        actions.user.mouse_move_relative_window(x_cur, y_cur)

    def game_press_key(key: str, dur: float = 0):
        "Presses key for specified time, if no dur given uses setting_keymouse_delay"
        if (dur == 0): dur = setting_keymouse_delay.get()
        actions.key(f"{key}:down")
        time.sleep(dur)
        actions.key(f"{key}:up")

    def game_press_mouse(button: int, dur: float = 0):
        "Holds mouse button for specified time, if no dur given uses setting_keymouse_delay"
        if (dur == 0): dur = setting_keymouse_delay.get()
        ctrl.mouse_click(button=button, down=True)
        time.sleep(dur)
        ctrl.mouse_click(button=button, up=True)

    def game_keys_down_and_up(keysDown: str, keysUp: str):
        """Holds a list of keys, and releases a list of keys"""
        for k in keysUp:
            #print(f'up: {k}')
            actions.key(f"{k}:up")

        for k in keysDown:
            #print(f'down: {k}')
            actions.key(f"{k}:down")

    def game_key_hold_down(keyDown: str, keyUp: str):
        "Hold down"
        if (len(keyUp) > 0): actions.key(f"{keyUp}:up")
        if (len(keyDown) > 0): actions.key(f"{keyDown}:down")


    def game_arrow_key_exclusive(dir: str):
        """Holds a direction, releases all others"""
        dirs = ["up", "down", "left", "right"]
        for d in dirs:
            actions.key(f"{d}:up")
        if (dir in dirs):
            actions.key(f"{dir}:down")


    def game_mouse_doubleclick(button: int, dur: float = 0):
        """Double clicks"""
        if (dur == 0): dur = 0.05
        actions.user.game_press_mouse(button, dur)
        time.sleep(dur)
        actions.user.game_press_mouse(button, dur)
    
    def game_mouse_drag(button: int, dur: float = 0):
        """Starts drags but first releases incase you wanted to re-start a drag"""
        if (dur == 0): dur = 0.01
        ctrl.mouse_click(button, up=True)
        time.sleep(dur)
        ctrl.mouse_click(button, down=True)


    # Game Utility
    def game_resize_window(): 
        "Resizes the active window using the settings, does nothing if settings not specified"
        x, y = (setting_game_window_size_x.get(), setting_game_window_size_y.get())
        if (x == 0 or y == 0): return
        print(f"Resizing to: {x},{y}")
        window = ui.active_window()
        window.resize(x, y)

    


def update_tag(voip_muted: bool):
    if voip_muted:
        ctx.tags = ["user.game_voip_muted"]
    else:
        ctx.tags = []


def voip_muted() -> bool:
    try:
        return actions.user.discord_get_mute_status()
    except:
        return True
