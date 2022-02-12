# PyTextStudio.py

![Example of PyTextStudio in use](https://i.imgur.com/pbagqR9.gif)

PyTextStudio is a program which allows you to create and use your own custom text expansions.

<<<<<<< HEAD
For users working with the Python file, the dependencies are `pyautogui`, `pynput`, `autocorrect`, and `pyperclip`.

If you want to use the program out-of-the-box with no Python installation, an easy-to-use `.exe` file has been included. Unfortunately, the `.exe` version does not have the autocorrect feature. This is because of an ongoing issue with the `autocorrect` library, where the English language cannot be downloaded when running from a compiled executable file. `pyspellchecker` has a similar issue. To use this feature, install Python, use `pip` to install all of the above dependencies, then launch the .py file.

I wrote this program because I noticed that most text expansion programs for Windows are locked behind a paywall, or restrict features to a premium version. I figured that I would make a Python-based "text studio" program that is completely free to use and edit.

**Version 2.1.0** includes many important quality of life improvements. Using text expansion and autocorrect no longer replaces the contents of the clipboard. This means that you can copy and paste as normal while using the program. [Click here to see the full release notes!](#version-history)
=======
For users working with the Python file, dependencies are `pyautogui`, `pynput`, and `autocorrect`.

An easy-to-use `.exe` file has been included, if you want to use the program out-of-the-box with no Python installation. Unfortunately, the `.exe` version does not have the autocorrect feature. This is because of an ongoing issue with the `autocorrect` library, where the English language cannot be downloaded when running from a compiled executable file. `pyspellchecker` has a similar issue. To use this feature, install Python, use `pip` to install all of the above dependencies, then launch the .py file.

I wrote this software because I noticed that most text expansion programs for Windows are locked behind a paywall, or restrict features to a premium version. I figured that I would make a Python-based "text studio" program that would be free to use and edit for anyone.

With the release of **version 2.0.0**, users can now create an unlimited number of save profiles! Use one profile for blazing-fast coding, and another for writing essays. With the ability to create an infinite amount of profiles, users can customize and organize to their heart's content. [Click here to see the release notes!](#version-history)
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7

# Usage

To use this program, click on the Code button and choose Download Zip. Then, extract the Zip folder. Launch the program using either `PyTextStudio.exe` or `PyTextStudio.py`.

The program will start with a main menu asking the user what they would like to do. 

```
<<<<<<< HEAD
 █▀█ █▄█ ▀█▀ █▀▀ ▀▄▀ ▀█▀ █▀ ▀█▀ █░█ █▀▄ █ █▀█  v2.1.0
=======
 █▀█ █▄█ ▀█▀ █▀▀ ▀▄▀ ▀█▀ █▀ ▀█▀ █░█ █▀▄ █ █▀█  v2.0.0
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7
 █▀▀ ░█░ ░█░ ██▄ █░█ ░█░ ▄█ ░█░ █▄█ █▄▀ █ █▄█

------------------------------------------------------

Welcome to PyTextStudio!
Remember to save regularly.

What would you like to do? (new/save/load/help):
```

## new


Typing in "new" and hitting enter will allow the user to create a new text expansion. The program will ask the user to type in a shortcut word. Next, the user is asked to assign the shortcut to an expanded word or phrase.

```
What would you like to do? (new/save/load/help): new

Enter a short word that you would like to expand: hw
Enter the text that you want the short word to expand into: Hello World!

Text shortcut registered! Type "hw" and hit Right Control to expand it into "Hello World!".
```

You can now convert the shortcut word into the expanded text by typing the short word, then hitting Right Control.

Example as shown above: if your shortcut text is "hw" and you assign the expanded text "Hello World!" to the shortcut, you can type "hw" and then hit Right Control.
This program will automatically convert the shortword into "Hello World!". This works in any window while PyTextStudio is running.

## save + load

Typing "save" in the main menu will allow you to store your active text expansions in a save file of your choice.

```
What would you like to do? (new/save/load/help): save

<<<<<<< HEAD


Where would you like to save?
Enter a profile name, then you will be able to access your data later using that name.
You can save to existing profiles, or type in a new name to create a new profile.

Enter a profile name: my first profile
=======
Where would you like to save? (file name without .txt): my first save file
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7


----------------------------------------------------------------------------------------

<<<<<<< HEAD
Your text expansions have been saved successfully as "my first profile". Type "load" and enter "my first profile" to access them later.
=======
Your text expansions have been saved successfully. Type "load" to access them later.
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7

Your short words list: ['hw']
Your expanded words list: ['Hello World!']

----------------------------------------------------------------------------------------
```

<<<<<<< HEAD
In the above example, the user saves their data to a new file named "my first profile.txt". This file is created by the program and kept in the "savefiles" folder.
=======
In the above example, the user saves their data to a new file named "my first save file.txt". This file is created by the program and kept in the "savefiles" folder.
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7

The user can load their saved data later by typing "load" in the main menu. 

```
What would you like to do? (new/save/load/help): load

<<<<<<< HEAD
Where would you like to load from? (profile name): my first profile
=======
Where would you like to load from? (file name without .txt): my first save file
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7


-----------------------------------------------------------------------

Your text expansions have been loaded successfully.

Your short words list: ['hw']
Your expanded words list: ['Hello World!']

-----------------------------------------------------------------------
```
<<<<<<< HEAD
In this example, the user loaded their previously saved data from "my first profile.txt". 
=======
In this example, the user loaded their previously saved data from "my first save file.txt". 
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7
You can create an unlimited number of save files, as long as they have different names. You can also save to one file an unlimited amount of times.

## help

<<<<<<< HEAD
Typing "help" in the main menu will print an informational paragraph teaching the user about the program's features and how to use them.

# Autocorrect

This program also has a built-in autocorrect tool. If you've just misspelled a word, hit F9 and the program will replace the text with the closest word match. This works in any window while PyTextStudio is running.
=======
Typing "help" in the main menu will print an informational paragraph teaching the user about the features of the program and how to use them.

# Autocorrect

This program also has a built-in autocorrect tool. If you've just misspelled a word, hit Right Alt and the program will replace the text with the closest word match. This works in any window while PyTextStudio is running.
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7

*This feature is not available in the .exe version of PyTextStudio.*

![Example of autocorrect in use](https://i.imgur.com/pHRwQFX.gif)

# Notes
If the user activates the save feature and types in the name of a file that doesn't exist yet, the program will simply create this file in the "savefiles" folder.

<<<<<<< HEAD
Entering "exit" instead of a profile name during the saving or loading process will cancel the process and return the user to the main menu.

This program has a feature to protect save data from being accidentally overwritten. If the user tries to save to a file that has potentially sensitive data from before, the program will ask them if they want to overwrite that data or combine the new expansions with the old data. This helps to prevent any unintended loss of user expansions.
=======
This program has a feature to protect save data from being accidentally overwritten. If the user tries to save to a file that has potentially sensitive data from before, the program will ask them if they want to overwrite that data or add the new expansions together with the old data. This helps to prevent any unintended loss of user expansions.

PyTextStudio can **crash on some systems** when the user loads data, then tries to use new text expansions that were created after loading. To avoid crashes in this situation, save your data, relaunch, then load again. 
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7



# Version History

<<<<<<< HEAD
## v2.1.0

Version 2.1.0 greatly improves the user experience of PyTextStudio. Using text expansion and autocorrect no longer replaces the text in the clipboard: users can now use this program while copying / pasting as normal. 

**All changes in v2.1.0:**
- Text expansion and autocorrect features no longer affect the most recent copied text in the clipboard.
    - A new dependency, `pyperclip`, is used to restore clipboard contents after expansion / autocorrect.
- Added additional instructions throughout the program which reduce confusion levels!
- Users can now back out of saving / loading by entering "exit" instead of a profile name. This returns them to the main menu.
- .lower() functions were added at various input points so that user inputs will still be valid if they contain uppercase letters.
- Changed default autocorrect hotkey to F9, since Right Alt seems to move the text cursor in Chrome now.

Version 2.1.0 was published in February 2022.

=======
>>>>>>> e2859466f1784a618877d425fa151557dd0f03b7
## v2.0.0

With the release of version 2.0.0 of PyTextStudio, users can now create an unlimited number of save profiles! Use one profile for blazing-fast coding, and another for writing essays. With the ability to create an infinite amount of profiles, users can customize and organize to their heart's content.

**Summary of changes in v2.0.0:**
- Completely overhauled save / load system. 
    - Added ability to create limitless number of save files.
    - Users can simply choose a name for their profile and they'll be able to load from there again.
    - The single `userShortcuts.txt` save file is gone. Your no longer have to save your data in one big pile.
    - Added new overwrite protection system for the new saving system.
- Visual changes to improve user experience.
    - Added brand new opening logo and message.
    - Changed separator characters for cleaner look.
- Streamlined code and fixed some crashes.

Version 2.0.0 was published in November 2020.

## v1.0.0

The initial release version of PyTextStudio! Launch features included text expansion capabilities, autocorrect, and basic saving / loading.

- Create and use an unlimited number of text expansions.
- Save and load using `userShortcuts.txt`. All data would be stored here.
- Autocorrect your last typed word using a hotkey.

Version 1.0.0 was published in August 2020.
