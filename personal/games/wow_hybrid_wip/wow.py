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

@mod.action_class
class MainActions:
    def game_wow_key(key: str):
        """I thought I might want a specific wow version of pressing a key, I did not end up doing anything..."""
        actions.key(key)

    def game_wow_step(key: str):
        """WoW step"""
        print(key)
        if key == "left": key = "q"
        if key == "right": key = "e"
        actions.user.game_hold_key(key, 0.2)

    def game_wow_spiral(key: str):
        """Attempts to navigate a spiral staircase"""
        # Nuked all this, too hard.


    

@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Click"""
        actions.mouse_click(0)
        

    def noise_trigger_hiss(active: bool):
        pass

