import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.apps.slaytheprincess = """
os: windows
and app.exe: SlaythePrincess.exe
"""


ctx = Context()
ctx.matches = """
app: slaytheprincess
"""

char_pos = {}

@mod.action_class
class UserActions:
    def game_stp_option_dir(dir: str, v: int):
        "Selects option"
        #x,y = actions.user.util_dir_to_xy(dir, v)
        for i in range(v):
            print (i)
            actions.user.game_hold_key(dir)
        #actions.user.mouse_move_relative(x*x_tile_gap, y*y_tile_gap)



@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Primary attack hold"""
        actions.user.game_hold_mouse(0)
        actions.user.grid_close()
        

    def noise_trigger_hiss(active: bool):
        """Primary attack hold"""
        pass
        