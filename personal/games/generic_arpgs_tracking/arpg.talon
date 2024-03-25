app: generic_arpg
mode: command
-

tag(): user.game_window

# 1922, 1112
settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.05
    user.game_window_size_x = 1920
    user.game_window_size_y = 1080
    key_hold = 32

# -  -- Actions
#^automatic press$:  user.game_handy_auto_presser("enter", 0.250)
#key(space): user.game_handy_auto_presser("enter", 0.250)

key(f14:down): key(4)
parrot(shush): key(3)
key(f15:down): key(2:down)
key(f15:up): key(2:up)
#key(f16:down): mouse_click(1) 
parrot(tut): mouse_click(1)

key(f16:down): user.game_arpg_toggle_move()

key(f17:down): key(n)
key(shift-f17:down): mouse_click(1)
key(f18:down): user.game_arpg_hold_last_key()
key(f18:up): user.game_arpg_release_last_key()
    #user.game_key_hold_down("", "shift")
    #user.mouse_drag_end()


#


one: user.game_arpg_down_key('1')
two: user.game_arpg_down_key('2')
three: user.game_arpg_down_key('3')
four: user.game_arpg_down_key('4')
five: user.game_arpg_down_key('5')

quench: user.game_arpg_press_key("1", true) 
whale: user.game_arpg_press_key("2", false) 
egg: user.game_arpg_press_key("3", false)
red: user.game_arpg_press_key("4", false) 
trap: user.game_arpg_press_key("5", false) 

passives: key(p)

heal: key(n)
follow: key(a)

loot: user.game_arpg_toggle_key('alt')
sell: user.game_arpg_toggle_key('shift')


# Mishearing
pit: mimic("five")
tale: mimic("whale")