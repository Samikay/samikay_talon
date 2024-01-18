app: ats
-

tag(): user.game_window

settings():
    user.mouse_move_amount = 20

# --- Actions
pan <user.arrow_key> [<user.n9>]: 
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

#Common misspeaks
brace: mimic("space")
bat: skip()
ten end: mimic("turn around")
ten red: mimic("turn around")


    
