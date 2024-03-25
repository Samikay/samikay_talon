app: generic_arpg
mode: user.game
-

tag(): user.game_window

settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.085
    user.game_window_size_x = 1920
    user.game_window_size_y = 1200
    key_hold = 32


key(f16:down): mimic("command mode")

key(f17:down):
    print("overriden")
     mouse_click(1)

key(shift-f17): mouse_click(1)

sit: key(i)

sell: user.game_arpg_toggle_key("shift")