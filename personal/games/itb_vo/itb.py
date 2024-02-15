import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.apps.intothebreach = """
os: windows
and app.exe: Breach.exe
"""


ctx = Context()
ctx.matches = """
app: intothebreach
"""

char_pos = {}

@mod.action_class
class UserActions:
    def game_itb_mouse_dir(dir: str, v: int):
        "Moves cursor"
        # center: 584,406 / up: 528,364 / l: 530:447 / d: 640,446 / r:643,364
        x1, x2 = (641, 696); y1, y2 = (361, 406)
        x_tile_gap = (x2 - x1); y_tile_gap = (y2 - y1)
        x,y = actions.user.util_dir_to_diag_xy(dir, v)
        actions.user.mouse_move_relative(x*x_tile_gap, y*y_tile_gap)
        
    def game_itb_confirm_deployment():
        """Confirms deployment"""
        x_cur, y_cur = actions.user.mouse_position_relative_window()
        actions.user.mouse_move_relative_window(113, 169)
        time.sleep(0.35)
        actions.mouse_click(0)
        time.sleep(0.1)
        actions.mouse_click(0)
        time.sleep(0.35)
        actions.user.mouse_move_relative_window(x_cur, y_cur)

    def game_itb_move_and_save(key: str):
        """Saves char pos"""
        global char_pos
        char_pos[key] = actions.user.mouse_position_relative_window()
        #print("would click")
        time.sleep(0.1)
        actions.mouse_click(0)
        actions.mouse_click(0)

    def game_itb_goto_char(key: str):
        """Goes to character"""
        global char_pos
        if (char_pos[key]):
            x_cur, y_cur = char_pos[key]
            actions.user.mouse_move_relative_window(x_cur, y_cur)
            actions.key(key)

@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Close grid if open"""
        actions.user.game_press_mouse(0)
        actions.user.grid_close()
        