# New Game Setup
- Copy an existing game folder to get started. Rename the .py and .talon files appropriately.
- Open the game, say `talon dump context` and click on the Talon icon in your tray -> **Scripting** -> **View Log**, note the name and/or title.
- In the .py file, change `mod.apps.[name]` to your [game name], and `app.exe: [game exe]` to your game's exe from the earlier command. Whatever you put for `mods.apps.[name]` copy into the ctx.matches `app` part.
- In the .talon file, change the very first line `app: [name]` to the same you put in ctx.matches.
- Make sure to save your changes to both files `Ctrl+S`
- Test out a command (something in the .talon file) in game to see if it worked! If it didn't, see **Commands not registering** below.

# Defining Commands
- games.py has some handy functions that should cover most usage.
- Check other game folders (such as ITB) for more examples to steal!
- Games tagged with "game_window" get some extra commands for free, see *_tags/game_window.talon*

# Handy commands defined elsewhere
- `print title` puts identifying information on the active window to **Scripting** -> **View Log**, such as the title, position and size.
- `copy relative`/`copy mouse` copies to clipboard (so you can follow up with `paste that`) and prints to log the current mouse position in the active window. You might want to define the game windows size (similar to *sap_vo/sap.talon*) so that `game window resize` will ensure all your mouse positions are the same if you happen to accidentally mess with the window size.
- `tool tip`/`stay` turns off eyetracking for 2.5s and then re-enables it so you can read tool tips/hovers.


# Commands Not Registering
- Makes sure all the names for things you defined match. In the .py that mod.apps.[name] = ctx.matches app: [name] and in the .talon app: [name]
- It's possible the .exe isn't matching, you can try matching against the title instead. See bg3.py for an example, to get the title say the command `print title` and check **Scripting** -> **View Log** for the result.
- Is your microphone unmuted/Talon awake? Don't laugh, it's happened to me many times...
