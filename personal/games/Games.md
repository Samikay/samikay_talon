# New Game Setup
- Copy an existing game folder to get started. Rename the .py and .talon files appropriately.
- Open the game, right click Talon icon in your tray, `Scripting` -> `Console (REPL)`
- Type `ui.apps()`, press `Ctrl-F` and type in parts of the game name until you get a match. Note the name of the .exe
- In the .py file, change `mod.apps.[game abbreviation]` to your [game abbreviation], and `app.exe: [game exe]` to your game's exe. Whatever you put for `mods.apps.[name]` copy into the ctx.matches `app` part.
- In the .talon file, change the very first line `app: [game abbreviation]` to the same you put in ctx.matches.
- Make sure to save your changes to both files `Ctrl+S`
- Test out a command (something in the .talon file) in game to see if it worked! If it didn't, see 

# Defining Commands
- Extra actions are defined in the module



# Commands Not Registering
- Makes sure all the names for things you defined match. In the .py that mod.apps.[name] = ctx.matches app: [name] and in the .talon app: [name]
- It's possible the .exe isn't matching, you can try matching against the title instead. See bg3.py for an example, to get the title say the command `print title` and check `Scripting` -> `View Log` for the result.
- Is your microphone unmuted/Talon awake? Don't laugh, it's happened to me many times...