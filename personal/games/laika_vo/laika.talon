app: laika
-

tag(): user.game_window

# 1922, 1112
settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.1
    user.game_window_size_x = 1920
    user.game_window_size_y = 1200
    key_hold = 32
    
# -  -- Actions
#^automatic press$:  user.game_handy_auto_presser("enter", 0.250)
#key(space): user.game_handy_auto_presser("enter", 0.250)

key(ctrl-shift-o:down): 
    user.game_keys_down_and_up("w", "")
    print("down")
key(ctrl-shift-o:up): 
    user.game_keys_down_and_up("", "w")
    print("up")
key(ctrl-shift-l:down): user.game_press_key("e")
key(ctrl-shift-l:up): user.game_press_key("e")
key(ctrl-shift-k:down): user.game_key_hold_down("space", "")
key(ctrl-shift-k:up): user.game_key_hold_down("", "space")

#noise(pop): user.game_press_key("e")

loot: user.game_arpg_toggle_key('alt')

equip: user.game_press_mouse(1, 0.05)

#misspeaks
trap: mimic('drag')
yank: mimic('drag')