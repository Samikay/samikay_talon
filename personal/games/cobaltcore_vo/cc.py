import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.apps.cobaltcore = """
os: windows
and app.exe: CobaltCore.exe
"""


ctx = Context()
ctx.matches = """
app: cobaltcore
"""

char_pos = {}

@mod.action_class
class UserActions:
    def game_cc_mouse_dir(dir: str, v: int):
        "Moves cursor"
        # center: 584,406 / up: 528,364 / l: 530:447 / d: 640,446 / r:643,364
        x1, x2 = (714, 954); y1, y2 = (50, 90)
        x_tile_gap = (x2 - x1); y_tile_gap = (y2 - y1)
        #distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        #print(f"distance {distance} tile_gap {584 - 535}")
        #tile_gap = distance
        y = 0
        x = 0
        if (dir == "up"): y = -1;
        if (dir == "down"): y = 1;
        if (dir == "left"): x = -1;
        if (dir == "right"): x = 1;

        x = x*v
        y = y*v

        actions.user.mouse_move_relative(x*x_tile_gap, y*y_tile_gap)



@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Primary attack hold"""
        actions.user.game_hold_mouse(0)
        actions.user.grid_close()
        
        

    def noise_trigger_hiss(active: bool):
        """Primary attack hold"""
        pass
        