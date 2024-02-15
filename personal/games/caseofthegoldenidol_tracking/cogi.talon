app: cogi
-

tag(): user.game_window

# 1922, 1112
settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.3
    user.game_window_size_x = 1922
    user.game_window_size_y = 1112
    key_hold = 32

# -  -- Actions
grab: mimic('drag')


empty: 
    mimic('wheel downer')
    sleep(1000ms)
    mimic('wheel stop')

sell here:
    mimic('wheel upper')
    sleep(1000ms)
    mimic('wheel stop')

fast forward:
    key(x:down)
    
normal speed:
    key(x:up)

#misspeaks
trap: mimic('drag')
yank: mimic('drag')
