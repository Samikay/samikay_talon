settings():
  user.mouse_move_amount = 30


key(ctrl-shift-o): user.toggle_speech()
key(ctrl-shift-l): user.mouse_control_toggle()
key(ctrl-shift-k): user.toggle_pop_click()

# Helpful 
(tool tip|stay): 
  user.mouse_control_toggle()
  sleep(2500ms)
  user.mouse_control_toggle()

hold [down] <user.modifiers>+: key("{modifiers}:down")
release <user.modifiers>+: key("{modifiers}:up")

# 'Righty' doesn't get picked up with the accuracy I'd like
right click: mouse_click(1)  

#Chrome
tab return: 
  key(ctrl-shift-a)
  sleep(150ms)
  key(enter)

# Youtube...
go right small: mimic("go right two times")
go right some: mimic("go right five times")
go right large: mimic("go right ten times")

# Copies to clipboard, also prints to log.
copy relative: user.copy_mouse_position_relative_window()

# Prints identifying information on active window, useful for context matching (better way, say: talon dump context), or with games/games.py: game_resize_window
print title: user.util_print_active_window()