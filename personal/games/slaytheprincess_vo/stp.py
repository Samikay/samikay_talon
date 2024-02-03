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
        
        for i in range(v):
            actions.user.game_hold_key(dir)
        



@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Close grid if open"""
        actions.user.game_hold_mouse(0)
        actions.user.grid_close()
        

    def noise_trigger_hiss(active: bool):
        """Stop accidental scrolling"""
        pass
        