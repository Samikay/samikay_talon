settings():
  user.mouse_move_amount = 30


key(ctrl-shift-o): user.toggle_speech()
key(ctrl-shift-l): user.mouse_control_toggle()
key(ctrl-shift-k): user.toggle_pop_click()

#Chrome
tab return: 
  key(ctrl-shift-a)
  sleep(150ms)
  key(enter)

hold down <user.modifiers>+: key("{modifiers}:down")
release <user.modifiers>+: key("{modifiers}:up")

# Youtube...
go right small: mimic("go right two times")
go right some: mimic("go right five times")
go right large: mimic("go right ten times")

# Copies to clipboard, also prints to log.
copy relative: user.copy_mouse_position_relative_window()

# Prints identifying information on active window, useful for context matching, or with game_resize_window
print title: user.util_print_active_window()


^game mode$:                user.game_mode_enable()

# Change air to something.
# change near to something.