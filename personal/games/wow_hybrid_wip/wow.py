import time

from talon import Module, Context, actions

self = actions.self

mod = Module()

mod.apps.wow = """
os: windows
and title: World of Warcraft
"""

ctx = Context()
ctx.matches = """
mode: user.game
app: wow
"""

ctx_frozen_mouse = Context()
ctx_frozen_mouse.matches = """
mode: user.game
app: wow
tag: user.eye_tracker_frozen
"""

# Release held mouse buttons for all key presses except these
dont_release = {"a", "b", "c", "d", "space"}

mod.list("wow_letter")
ctx.lists["user.wow_letter"] = {
    "made": "m"
}

@mod.action_class
class MainActions:
    def game_wow_key(key: str):
        """Diablo implementation of pressing a key"""
        if ":" not in key and key not in dont_release:
            actions.user.mouse_release_held_buttons()
        #actions.next(key)
        actions.key(key)

    def game_wow_key_holdfor(key: str, sleep: float):
        """Hold key for {sleep} amount of time."""
        actions.key(f"{key}:down")
        time.sleep(sleep)
        actions.key(f"{key}:up")

    def game_wow_step(key: str):
        """WoW step"""
        print(key)
        if key == "left": key = "q"
        if key == "right": key = "e"
        self.game_wow_key_holdfor(key, 0.2)

    def game_wow_spiral(key: str):
        """Attempts to navigate a spiral staircase"""
        
        
    
    def game_wow_180():
        """Turns 180"""
        self.game_wow_key_holdfor("a", 1)


    

@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Primary attack hold"""
        actions.mouse_click(0)
        

    def noise_trigger_hiss(active: bool):
        """Primary attack hold"""
        #actions.key()
        pass



@ctx_frozen_mouse.action_class("user")
class FrozenMouseActions:
    def noise_trigger_pop():
        """Primary attack hold"""
        actions.mouse_click(0)
        actions.mouse_drag(0)

    def noise_trigger_hiss(active: bool):
        """Primary attack hold"""
        pass


def mouse_click(button: int):
    # Can't hold two buttons at the same time
    actions.user.mouse_release_held_buttons()
    actions.mouse_click(button)
