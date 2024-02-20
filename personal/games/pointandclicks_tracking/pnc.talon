app: generic_pnc
-

tag(): user.game_window

# 1922, 1112
settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.2
    user.game_window_size_x = 1920
    user.game_window_size_y = 1080
    key_hold = 32

# -  -- Actions
#^automatic press$:  user.game_handy_auto_presser("enter", 0.250)
#key(space): user.game_handy_auto_presser("enter", 0.250)

<user.arrow_key> [<user.n9>]: 
    mod = n9 or 1
    user.game_press_key(user.util_dir_to_wasd(arrow_key), 0.1 * mod)

#misspeaks
trap: mimic('drag')
yank: mimic('drag')