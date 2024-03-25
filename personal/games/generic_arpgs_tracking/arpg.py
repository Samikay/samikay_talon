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
  
last_pressed_key = ""

@mod.action_class
class MainActions:
    def game_arpg_down_key(key: str) -> bool:
        """Holds the key"""
        inputHolder.release_key()
        return inputHolder.hold_key(key)

    def game_arpg_toggle_key(key: str) -> bool:
        "Title"
        return inputHolder.hold_key(key)

    def game_arpg_press_key(key: str, remember: bool = True):
        """Can remember the last key press to repeat elsewhere."""
        global last_pressed_key
        inputHolder.release_key()
        if (remember): 
            last_pressed_key = key
        actions.key(key)


    def game_arpg_hold_last_key():
        "Title"
        global last_pressed_key
        print("last pressed: " + last_pressed_key)
        if (inputHolder.get_last_held() != last_pressed_key):
            inputHolder.release_key()
            inputHolder.hold_key(last_pressed_key)

        isSentinel = False
        if (isSentinel):
            inputHolder.interval_click_while_holding(1)
            pass


    def game_arpg_release_last_key():
        "Title"
        inputHolder.release_key()

    def game_arpg_toggle_move():
        "Title"
        inputHolder.release_key()
        inputHolder.hold_click(0)





@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Always run"""
        inputHolder.release_key()
        if (inputHolder.is_holding_click()):
            actions.key("2")
        else:
            actions.user.game_press_mouse(0)
            inputHolder.resetClick()

        
        

    def noise_trigger_hiss(active: bool):
        """Null out"""
        if (active):
          inputHolder.release_key()
          inputHolder.resetClick()
          inputHolder.hold_click(0)
          pass
        pass

    
      

