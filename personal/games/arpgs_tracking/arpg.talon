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

key(ctrl-shift-o:down): 
    mouse_drag(0)
key(ctrl-shift-o:up): 
    user.mouse_drag_end()

key(ctrl-shift-k:down): 
    mouse_drag(0)
key(ctrl-shift-k:up): 
    user.mouse_drag_end()

one: user.game_arpg_toggle_key('1')
two: user.game_arpg_toggle_key('2')
three: user.game_arpg_toggle_key('3')
four: user.game_arpg_toggle_key('4')
five: user.game_arpg_toggle_key('5')

whale: user.game_press_key("2")
egg: user.game_press_key("3")
red: user.game_press_key("4")

loot: user.game_arpg_toggle_key('alt')

equip: user.game_press_mouse(1, 0.05)

#misspeaks
trap: mimic('drag')
yank: mimic('drag')