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

@mod.action_class
class UserActions:
    def game_cc_mouse_dir(dir: str, v: int):
        "Moves cursor"
        x1, x2 = (714, 954); y1, y2 = (50, 90)
        x_tile_gap = (x2 - x1); y_tile_gap = (y2 - y1)

        #x_tile_gap = (900 - 714) #Uncomment if you take +2 card draw every turn
    
        x,y = actions.user.util_dir_to_xy(dir, v)
        actions.user.mouse_move_relative(x*x_tile_gap, y*y_tile_gap)



@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Close grid if open"""
        actions.user.game_press_mouse(0)
        actions.user.grid_close()
        

    def noise_trigger_hiss(active: bool):
        """Null out"""
        pass
        