mode: user.game
app: wow
-

settings():
    speech.timeout = 0.085

stop: 
    key(w)
    key(q)
    key(e)
    key(s)
    key(d)
    key(a)

run:
    key(s:up)
    key(e:up)
    key(q:up)
    key(w:down)
left: 
    key(e:up)
    key(q:down)
right: 
    key(q:up)
    key(e:down)
back: 
    key(w:up)
    key(s:down)

step <user.arrow_key>: user.game_wow_step(arrow_key)
    
look left:  user.game_wow_step("a")
look right: user.game_wow_step("d")
    

turn left: user.game_wow_key_holdfor("a", 0.5)
turn right: user.game_wow_key_holdfor("d", 0.5)
turn around: user.game_wow_180()

center: user.mouse_move_center_active_window()
use: mouse_click(1)
select: mouse_click(0)

#Warlock
bolt: user.mouse_scroll_up()
hand: user.mouse_scroll_down()
demon: key(5)
tyrant: key(shift-r)
strength: key(shift-t)
trinket: key(shift-4)
power: key(shift-s)
snipe: key(shift-d)
blast: key(shift-3)
defend: key(shift-g)


mouse four: mouse_click(4)
mouse five: mouse_click(5)

mouse loot: user.mouse_move_relative_window(1299, 1158)
mouse quest: user.mouse_move_relative_window(1670, 937)

spiral right: user.game_wow_spiral("right")

copy relative: user.copy_mouse_position_relative_window()

{user.prose_formatter} <user.prose>$: user.insert_formatted(prose, prose_formatter)

# Modifier(s) + key: "control air" or "control win left"
#<user.modifier_key> <user.unmodified_key>: user.game_wow_key("{modifier_key}-{unmodified_key}")
#<user.letter>: user.game_wow_key(letter)
#press <user.key>:
#    print(key)
#    user.game_wow_key(key)

##  Copied directly from core/keys
#go <user.arrow_keys>: user.move_cursor(arrow_keys) #might not want conflicting with other arrow commands.
<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]:
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
# for key combos consisting only of modifiers, eg. `press super`.
press <user.modifiers>: key(modifiers)
# for consistency with dictation mode and explicit arrow keys if you need them.
press <user.keys>: key(keys)

<user.number_string>: "{number_string}"

##  Copied directly from personal/plugin/mouse.talon
mouse <user.arrow_key> [<user.n9>]: 
    modifier = n9 or 1
    user.mouse_move_dir(arrow_key, 1 * modifier)