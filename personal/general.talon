settings():
  user.mouse_move_amount = 30


key(ctrl-shift-o): user.toggle_speech()

hold down <user.modifiers>+: key("{modifiers}:down")
release <user.modifiers>+: key("{modifiers}:up")

go right small: mimic("go right two times")
go right some: mimic("go right five times")
go right large: mimic("go right ten times")

copy relative: user.copy_mouse_position_relative_window()

^game mode$:                user.game_mode_enable()