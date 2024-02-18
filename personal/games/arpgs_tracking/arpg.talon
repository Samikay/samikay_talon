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

key(f16:down): 
    user.game_key_hold_down("shift", "")
    mouse_drag(0)
key(f16:up): 
    user.game_key_hold_down("", "shift")
    user.mouse_drag_end()

key(f14:down): 
    mouse_drag(0)
key(f14:up): 
    user.mouse_drag_end()

one: user.game_arpg_toggle_key('1')
two: user.game_arpg_toggle_key('2')
three: user.game_arpg_toggle_key('3')
four: user.game_arpg_toggle_key('4')
five: user.game_arpg_toggle_key('5')

egg: user.game_press_key("3")

heal: user.game_press_key('n')
follow: user.game_press_key('a')

loot: user.game_arpg_toggle_key('alt')

equip: user.game_press_mouse(1, 0.05)