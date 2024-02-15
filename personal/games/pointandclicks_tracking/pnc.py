import time

from talon import Module, Context, actions, ctrl
from .._handy.input_holder import InputHolder

mod = Module()

mod.apps.generic_pnc = """
os: windows
and title: Grim Fandango
"""

mod.apps.generic_pnc = """
os: windows
and title: /Chants of Sennaar/i
"""


ctx = Context()
ctx.matches = """
app: generic_pnc
"""

inputHolder = InputHolder()

@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        ctrl.mouse_click(0, down=True)
        time.sleep(0.05)
        ctrl.mouse_click(0, up=True)

    def noise_trigger_hiss(active: bool):
        """Null out"""
        if (active):
          #actions.user.game_mouse_drag(0)
          #actions.user.game_mouse_doubleclick(0)
          #actions.user.game_ double_click()
          inputHolder.hold_click(2)
          pass
        pass
      
  