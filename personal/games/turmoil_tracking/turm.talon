app: turmoil
-

tag(): user.game_window

# Assumes 2560x1440p for mouse positions.
settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.2
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
