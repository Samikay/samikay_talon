app: generic_arpg
mode: sleep
-

tag(): user.game_window

settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.085
    user.game_window_size_x = 1920
    user.game_window_size_y = 1200
    key_hold = 32

key(f14:down): key(2)
parrot(tut): key(3)
key(f15:down): key(4:down)
key(f15:up): key(4:up)
key(f16:down): mouse_click(1) 

key(f17:down): key(n)
key(f18:down): user.game_arpg_hold_last_key()
key(f18:up): user.game_arpg_release_last_key()