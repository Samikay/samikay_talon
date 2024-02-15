app: generic_arpg
-

tag(): user.game_window

# 1922, 1112
settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.1
    user.game_window_size_x = 1920
    user.game_window_size_y = 1080
    key_hold = 32
    

# -  -- Actions
#^automatic press$:  user.game_handy_auto_presser("enter", 0.250)
#key(space): user.game_handy_auto_presser("enter", 0.250)

loot: user.game_arpg_toggle_key('alt')

equip: user.game_press_mouse(1, 0.05)

#misspeaks
trap: mimic('drag')
yank: mimic('drag')