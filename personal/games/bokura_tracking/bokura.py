import time

from talon import Module, Context, actions, cron, ui
from .._handy.mouse_region_handler import MouseRegionHandler

self = actions.self

mod = Module()

mod.apps.bokura = """
os: windows
and app.exe: BOKURA.exe
"""

mod.apps.bokura = """
os: windows
and title: /BOKURA/i
"""

ctx = Context()
ctx.matches = """
app: bokura
"""


hold_rmb = False

@mod.action_class
class MainActions:
    def game_bokura_toggle_enter() -> bool:
        """Toggles enter"""
        global hold_rmb
        hold_rmb = not hold_rmb
        if (hold_rmb): actions.key(f"enter:down")
        if (not hold_rmb): actions.key(f"enter:up")
        return hold_rmb

    def game_bokura_setup_regions():
        """Setup"""
        regionHandler.setup(221, 120) #221, 120


regionHandler = MouseRegionHandler()
move_job = None

@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        actions.mouse_click(0)

        key = regionHandler.which_dir_exclusive(left = "a", right = "d", up = "w")
        actions.user.game_keys_down_and_up(f"{key}", "")
        actions.user.game_press_key("space")
        actions.user.game_keys_down_and_up("", f"{key}")
        

    def noise_trigger_hiss(active: bool):
        if (active):
            move_continuous()
        else:
            stop_move()
            actions.user.game_keys_down_and_up("", "wasd")
            time.sleep(0.025)
            actions.user.game_keys_down_and_up("", "wasd")


        pass

def move_continuous():
    global move_job 
    if move_job is None:  
        move_job = cron.interval("25ms", move_continuous_helper)

def stop_move():
    global move_job
    if move_job:
        cron.cancel(move_job)
        move_job = None

def move_continuous_helper():
    if move_job:
        keys = regionHandler.which_inclusive()
        actions.user.game_keys_down_and_up(keys, "wasd")