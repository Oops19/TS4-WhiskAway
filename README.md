# TS4 Whisk Away

This is a tiny mod to move sims either to a different household or purge them from the game.
Unlike sims which die this mod simply removes the sims, no one will be happy or sad.

It is a cheat interaction and available for all sims, not limited to babies.
Some menu options might make no sense for adult sims.

There is no check for standard sims (like Rey, Hondo, ...) which should probably not be whisked away.

The 'Whisk Away' main options will move the sim to a different household.
* 'Super-Nanny' is a female to care about minors.
* 'Family' needs at least one male and female sim (teen and/or young adult). The agency believes that a male and a female sim is needed.
  * All other options will randomly select one or the other.
  * In case no Family can be found the agency looks for a Super-Nanny.
  * In case no Super-Nanny an be found this sim will not be whisked away.

There is no 'Undo' while the sim can be found in a random household unless TS4 clears un-played households.

After clicking on 'More ...' the 'advanced' options will be visible within three sub menus.
All available options will remove the sim from the game, there is no undo.
There are no (violence, fire, abduction, ...) animations, the sim will simply be removed.

## Age limitation
Child and younger sims can only whisk away sims with the same and or younger sims.
Teen to elder sims can whisk away random sims.

## Family limitations
Only family members can whisk away child or younger sims.
Mean and/or insane sims should be able to whisk away random child sims, anyhow this is currently not implemented.



# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.111.102, S4CL 3.9, TS4Lib 0.3.33.
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2024 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
