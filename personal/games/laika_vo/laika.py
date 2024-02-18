import time

from talon import Module, Context, actions, ctrl
from .._handy.input_holder import InputHolder

mod = Module()

mod.apps.laika = """
os: windows
and title: /Laika/
"""


ctx = Context()
ctx.matches = """
app: laika
"""

inputHolder = InputHolder()
        


@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Always run"""
        #actions.user.game_press_mouse(0)
        inputHolder.hold_click(0)
        #inputHolder.reset(heldKey = False, heldClick = True)
        

    def noise_trigger_hiss(active: bool):
        """Null out"""
        if (active):
          actions.user.game_key_hold_down("space", "")
          pass
        else:
          actions.user.game_key_hold_down("", "space")
        pass
      

