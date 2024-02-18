import time

from talon import Module, Context, actions, ui, cron, ctrl
from .._handy.mouse_region_handler import MouseRegionHandler

self = actions.self

mod = Module()

mod.apps.boi = """
os: windows
and app.exe: isaac-ng.exe
"""

ctx = Context()
ctx.matches = """
app: boi
"""

hold_rmb = False

@mod.action_class
class MainActions:
    def game_isaac_toggle_move() -> bool:
        """Holds RMB to move isaac to mouse cursor, courtesy of this mod: https://steamcommunity.com/sharedfiles/filedetails/?id=2897857568"""
        global hold_rmb
        hold_rmb = not hold_rmb
        #if (hold_rmb): ctrl.mouse_click(1, down=True)
        #if (not hold_rmb): ctrl.mouse_click(1, up=True)
        return hold_rmb

    def game_isaac_setup_regions():
        """Setup"""
        regionHandler.setup(120, 120) #221, 120



regionHandler = MouseRegionHandler()
move_job = None

@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        print("hello")
        actions.mouse_click(0)
        pop_shoot()
        return

        

    def noise_trigger_hiss(active: bool):
        if (active):
            move_continuous()
        else:
            stop_move()
            actions.user.game_keys_down_and_up("", "wasd")
            time.sleep(0.025)
            actions.user.game_keys_down_and_up("", "wasd")


        pass

def pop_move():
    isMoving = actions.user.game_isaac_toggle_move()
    if (isMoving): 
        move_continuous()
    else:
        stop_move()
        actions.user.game_keys_down_and_up("", "wasd")
        time.sleep(0.025)
        actions.user.game_keys_down_and_up("", "wasd")

def pop_shoot():
    arrow = regionHandler.which_dir_exclusive()
    actions.user.game_arrow_key_exclusive(arrow)


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
        print(keys)
        actions.user.game_keys_down_and_up(keys, "wasd")