import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.mode("game", "Used to play games")
mod.tag("game_voip_muted", "Signals that game voice chat is muted")

self = actions.self

setting_keymouse_delay = mod.setting(
    "game_keymouse_delay",
    type=float,
    default=0.1,
    desc="The amount to move the mouse in the current window",
)


ctx = Context()
ctx.matches = r"""
mode: user.game
"""

ctx.settings = {
    #"speech.timeout": 0.05,
}


@ctx.action_class("speech")
class SpeechActions:
    def disable():
        actions.mode.save()
        actions.mode.disable("user.game")
        actions.mode.enable("sleep")


@mod.action_class
class Actions:
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

    

    def game_move_click(x: int, y: int):
        """Moves mouse and clicks"""
        actions.user.mouse_move_relative_window(x, y)
        time.sleep(0.25) #give time for ui to respond
        ctrl.mouse_click(button=0, down=True)
        time.sleep(0.1)
        ctrl.mouse_click(button=0, up=True)
    
    def game_move_click_return(x: int, y: int):
        """Moves mouse, clicks, returns"""
        x_cur, y_cur = actions.user.mouse_position_relative_window()
        self.game_move_click(x, y)
        actions.user.mouse_move_relative_window(x_cur, y_cur)

    def game_hold_key(key: str, dur: float = 0):
        "Holds key for specified time, if no dur given uses setting_keymouse_delay"
        if (dur == 0): dur = setting_keymouse_delay.get()
        actions.key(f"{key}:down")
        time.sleep(dur)
        actions.key(f"{key}:up")

    def game_hold_mouse(button: int, dur: float = 0):
        "Holds mouse button for specified time, if no dur given uses setting_keymouse_delay"
        if (dur == 0): dur = setting_keymouse_delay.get()
        ctrl.mouse_click(button=button, down=True)
        time.sleep(dur)
        ctrl.mouse_click(button=button, up=True)

    


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
