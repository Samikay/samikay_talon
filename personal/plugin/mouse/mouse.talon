mouse <user.arrow_key> [<user.n9>]: 
  modifier = n9 or 1
  user.mouse_move_dir(arrow_key, 1 * modifier)

  # Eye tracking
track on:                   user.mouse_control_toggle(true)
track off:                  user.mouse_control_toggle(false)
tracking:                   user.mouse_control_toggle()
track gaze:                 tracking.control_gaze_toggle(true)
track head:                 tracking.control_gaze_toggle(false)
track debug:                tracking.control_debug_toggle()
track calibrate:            tracking.calibrate()