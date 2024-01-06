import os
import time

from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, ui
from talon_plugins import eye_zoom_mouse

self = actions.self

mod = Module()
ctx = Context()

setting_mouse_move_amount = mod.setting(
    "mouse_move_amount",
    type=int,
    default=40,
    desc="The amount to move the mouse",
)

setting_mouse_move_window_amount = mod.setting(
    "mouse_move_relative_amount",
    type=int,
    default=40,
    desc="The amount to move the mouse in the current window",
)

@mod.action_class
class ExtendActions:
    def mouse_move_relative(x: int, y: int):
        """Move the mouse relative to its current position"""
        x_cur, y_cur = ctrl.mouse_pos()
        actions.mouse_move(x_cur+x, y_cur+y)

    def mouse_position_relative_window():
        """Get current mouse position in window"""
        x, y = ctrl.mouse_pos()
        rect = ui.active_window().rect

        return x - rect.left, y-rect.top


    def copy_mouse_position_relative_window():
        """Copy the current mouse position coordinates"""
        x, y = self.mouse_position_relative_window()
        text = f"{x},{y}"
        clip.set_text(text)
        print("Mouse pos: " + text)

    def mouse_move_relative_window(x: int, y: int):
        """Move the mouse to a point relative to the current window"""
        rect = ui.active_window().rect
        actions.mouse_move(x+rect.left, y+rect.top)

    def mouse_release():
        """Release drag"""
        ctrl.mouse_click(up=True)
        current_exe = ui.active_app().exe.lower()

    def mouse_release_held_buttons() -> bool:
        """Release held mouse buttons"""
        buttons = ctrl.mouse_buttons_down()
        if buttons:
            for button in buttons:
                actions.mouse_release(button)
            return True
        return False

    def mouse_sap_drag(x: int, y: int):
        """Dragging SAP animals."""
        ctrl.mouse_click(down=True)
        time.sleep(0.550)
        actions.user.mouse_drag(0)
        time.sleep(0.250)
        self.mouse_move_relative(setting_mouse_move_amount.get()*x, setting_mouse_move_amount.get()*y)
        time.sleep(0.550)
        actions.user.mouse_drag_end()
        #self.mouse_release()

    def mouse_move_times(x: int, y: int):
        """Mouse movement"""
        self.mouse_move_relative(x * setting_mouse_move_amount.get(), y * setting_mouse_move_amount.get())