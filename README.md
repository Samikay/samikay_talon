A gamer's Talon Voice repo.

## How To Use

1. Install & Run Talon ( https://talonvoice.com/ ).
2. Click on the Talon icon on your task bar, `Speech Recognition` -> `Install Conformer D`
![Talon Tray](https://i.imgur.com/NgwUvGS.jpeg)
3. Click on the Talon icon on your task bar, `Scripting` -> `Open Talon Home`
4. Download this repo as a ZIP by clicking on the green `Code` button, then `Download ZIP`. If you are more technical, you can do this the 'expected' way.
5. Unzip the contents into the `user` folder.
![Talon Folder Setup](https://i.imgur.com/CvAtHnm.jpeg)
6. Learn Talon :P The [community repo](https://github.com/talonhub/community?tab=readme-ov-file#getting-started-with-talon) can help with that.

## Games
Has support for the following, see [personal/games/README](https://github.com/Samikay/samikay_talon/tree/main/personal/games) for adding more:
- Super Auto Pets (Voice Only)
- Into The Breach (Voice Only)
- Cobalt Core (Voice Only)
- Slay The Princess (Voice Only)
- WoW Classic (90% Voice Only)
- Against The Storm (Eye tracking)
- Baldur's Gate 3 (Eye tracking)


## Helpful
[Talon Wiki: User File Sets](https://talon.wiki/talon_user_file_sets/)

# Credits

- [Talon Community](https://github.com/talonhub/community) 
- [David Tejada - Rango](https://github.com/david-tejada/rango-talon)
- [Andreas Arvidsson](https://github.com/AndreasArvidsson/andreas-talon) (who plays Diablo 3 with Talon, very cool!)


# Subtree setup
```
git remote add -f community https://github.com/talonhub/community
git remote add -f rango-talon https://github.com/david-tejada/rango-talon

git subtree add --prefix community community main --squash
git subtree add --prefix rango-talon rango-talon main --squash
```

# Subtree Maintenance
## Pulling new changes
```
git fetch community main
git subtree pull --prefix community community main --squash

git fetch rango-talon main
git subtree pull --prefix rango-talon rango-talon main --squash
```

