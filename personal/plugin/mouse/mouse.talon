mouse right [<user.n20>]: 
  modifier = n20 or 1
  user.mouse_move_times(1 * modifier, 0)

mouse left [<user.n20>]: 
  modifier = n20 or 1
  user.mouse_move_times(-1 * modifier, 0)

mouse up [<user.n20>]: 
  modifier = n20 or 1
  user.mouse_move_times(0, -1 * modifier)

mouse down [<user.n20>]: 
  modifier = n20 or 1
  user.mouse_move_times(0, 1 * modifier)

  # Eye tracking
track on:                   user.mouse_control_toggle(true)
track off:                  user.mouse_control_toggle(false)
tracking:                   user.mouse_control_toggle()
track gaze:                 tracking.control_gaze_toggle(true)
track head:                 tracking.control_gaze_toggle(false)
track debug:                tracking.control_debug_toggle()
track calibrate:            tracking.calibrate()