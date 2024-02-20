import time

from talon import Module, Context, actions, ctrl
from .._handy.input_holder import InputHolder
from .._handy.mouse_region_handler import MouseRegionHandler

mod = Module()

mod.apps.generic_arpg = """
os: windows
and title: Chronicon
"""

mod.apps.generic_arpg = """
os: windows
and title: Last Epoch
"""


ctx = Context()
ctx.matches = """
app: generic_arpg
"""

inputHolder = InputHolder(True)

@mod.action_class
class MainActions:
    def game_arpg_toggle_key(key: str) -> bool:
        """Holds the key"""
        inputHolder.release_key()
        return inputHolder.hold_key(key)

    def game_arpg_hold_last_key():
        "Title"
        global last_pressed_key
        print("last pressed: " + last_pressed_key)
        inputHolder.release_key()
        inputHolder.hold_key(last_pressed_key)

    def game_arpg_release_last_key():
        "Title"
        inputHolder.release_key()



        
last_pressed_key = ""

@ctx.action_class("user")
class OverrideActions:
    def game_press_key(key: str, dur: float = 0):
        global last_pressed_key
        inputHolder.release_key()
        last_pressed_key = key
        actions.key(key)

        

    def noise_trigger_pop():
        """Always run"""
        inputHolder.release_key()
        actions.user.game_press_mouse(0)
        inputHolder.reset(heldKey = False, heldClick = True)
        

    def noise_trigger_hiss(active: bool):
        """Null out"""
        if (active):
          inputHolder.release_key()
          inputHolder.reset(heldKey = False, heldClick = True)
          inputHolder.hold_click(0)
          pass
        pass
      

