app: baldursgate3
-

tag(): user.game_window

settings():
    user.mouse_move_amount = 20

# --- Actions
<user.arrow_key> [<user.n9>]: user.mouse_move_dir(arrow_key, n9 or 1)

pan <user.arrow_key> [<user.n9>]: 
    mod = n9 or 1
    user.game_hold_key(arrow_key, 0.25 * mod)

look left [<user.n9>]: 
    mod = n9 or 1
    user.game_hold_key("q", 0.35 * mod)

look right [<user.n9>]: 
    mod = n9 or 1
    user.game_hold_key("e", 0.35 * mod)

turn around: user.game_hold_key("e", 0.35*5)
turn right: mimic("look right four")
turn left: mimic("look left four")


hold alt: 
    key(alt:up)
    key(alt:down)



spell <user.arrow_key> [<user.n9>]: 
    mod = n9 or 1
    user.mouse_move_dir(arrow_key, 3 * mod)


brace: mimic("space")
bat: skip()
ten end: mimic("turn around")
ten red: mimic("turn around")

# Skip cutscenes
skip:
    mouse_click(0)
    sleep(1s)
    mouse_click(0)
    sleep(50ms)
