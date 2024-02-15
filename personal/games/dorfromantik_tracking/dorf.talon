app: dorf
-

tag(): user.game_window

# Assumes 2560x1440p for mouse positions.
settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.2
    key_hold = 32

# -  -- Actions
<user.arrow_key> [<user.n9>]: 
    mod = n9 or 1
    user.game_press_key(user.util_dir_to_wasd(arrow_key), 0.5 * mod)

look left [<user.n9>]: 
    mod = n9 or 1
    user.game_press_key("q", 0.35 * mod)

look right [<user.n9>]: 
    mod = n9 or 1
    user.game_press_key("e", 0.35 * mod)

turn around: mimic("look right four")
turn right: mimic("look right two")
turn left: mimic("look left two")

close: mimic('escape')
grab: mimic('hold down shift')
working: mimic('hold down alt')
release: 
    mimic('release alt')
    mimic('release shift')

center:
    mimic("harp")
    sleep(50ms)
    mimic("wheel downer")
    sleep(750ms)
    mimic("wheel stop")

#Common misspeaks
plus: mimic('close')
pause: mimic('space')
brace: mimic("space")
bat: skip()
dot: mimic("down")
ten end: mimic("turn around")
ten red: mimic("turn around")
^tab$: mimic('down')


    
