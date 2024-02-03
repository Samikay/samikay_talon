app: ats
-

tag(): user.game_window

settings():
    user.mouse_move_amount = 60
    speech.timeout = 0.2

# -  -- Actions
<user.arrow_key> [<user.n9>]: 
    mod = n9 or 1
    user.game_hold_key(user.util_dir_to_wasd(arrow_key), 0.5 * mod)

look left [<user.n9>]: 
    mod = n9 or 1
    user.game_hold_key("q", 0.35 * mod)

look right [<user.n9>]: 
    mod = n9 or 1
    user.game_hold_key("e", 0.35 * mod)

turn around: mimic("look right four")
turn right: mimic("look right two")
turn left: mimic("look left two")

close: mimic('escape')
grab: mimic('hold down shift')
working: mimic('hold down alt')
release: 
    mimic('release alt')
    mimic('release shift')

food: user.game_move_click(1049,1368)
useful: user.game_move_click(1203,1357)
house: user.game_move_click(1134,1357)
camps: user.game_move_click(1008,1357)
roads: user.game_move_click(938,1358)
services: user.game_move_click(1271,1351)

rotate:
    mimic("red")
    sleep(50ms)
    mimic("red")
    sleep(50ms)
    mimic("red")

zoom out:
    mimic("wheel downer")
    sleep(750ms)
    mimic("wheel stop")

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


    
