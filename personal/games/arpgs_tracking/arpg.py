import time

from talon import Module, Context, actions, ctrl
from .._handy.input_holder import InputHolder

mod = Module()

mod.apps.generic_arpg = """
os: windows
and title: Chronicon
"""


ctx = Context()
ctx.matches = """
app: generic_arpg
"""

inputHolder = InputHolder()

@mod.action_class
class MainActions:
    def game_arpg_toggle_key(key: str) -> bool:
        """Holds the key"""
        return inputHolder.hold_key(key)
        


@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Always run"""
        actions.user.game_press_mouse(0)
        inputHolder.reset(heldKey = False, heldClick = True)
        

    def noise_trigger_hiss(active: bool):
        """Null out"""
        if (active):
          inputHolder.hold_click(0)
          pass
        pass
      

