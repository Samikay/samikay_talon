

import time

from talon import Module, Context, actions, cron, ui


self = actions.self

mod = Module()
auto_job = None
key_to_press = "enter"

@mod.action_class
class MainActions:

    def game_handy_auto_presser(key: str, frequency: float):
        """Presses a key every x seconds"""
        press_continuous(key, (frequency * 1000))

    def game_handy_auto_stop():
      """ Stops automatic pressing"""
      stop_auto_press()

        
def press_continuous(key: str, freq: int):
    global auto_job, key_to_press
    key_to_press = key
    if auto_job is None:  
        auto_job = cron.interval(f"{freq:.0f}ms", press_continuous_helper)
    else:
        stop_auto_press()

def stop_auto_press():
    global auto_job
    if auto_job:
        cron.cancel(auto_job)
        auto_job = None

def press_continuous_helper():
    global key_to_press
    if auto_job:
        actions.user.game_press_key(f"{key_to_press}")