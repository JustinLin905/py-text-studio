# PyTextStudio.py

![Example of PyTextStudio in use](https://i.imgur.com/pbagqR9.gif)

PyTextStudio is a minimal program which allows users to use, save, and load their own custom text expansions.

For users working with the Python file, dependencies are `pyautogui`, `pynput`, and `autocorrect`.

An easy-to-use `.exe` file has been included, if you want to use the program out-of-the-box with no Python installation. Unfortunately, the `.exe` version does not have the autocorrect feature. This is because of an ongoing issue with the `autocorrect` library, where the English language cannot be downloaded when running from a compiled executable file. `pyspellchecker` has a similar issue. To use this feature, install Python and use `pip` to install all of the above dependencies.

I wrote this software because I noticed that most text expansion programs for Windows are locked behind a paywall, or restrict features to a premium version. I figured that I would make a simple Python-based "text studio" program that would be free to use and edit for anyone.


# Usage

To use this program, click on the Code button and choose Download Zip. Then, extract the Zip folder. Launch the program using either the `PyTextStudio.exe` or the `PyTextStudio.py` file.

The program will start with a main menu asking the user what they would like to do. 

```
Welcome to PyTextStudio!

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

Typing "save" in the main menu will store your active text expansions in the included `userShortcuts.txt` file. 

The user can exit the program and load their saved data later by typing "load" in the main menu. This will activate previously saved text expansions and make them usable again in the current instance. 

## help

Typing "help" in the main menu will print an informational paragraph teaching the user about the features of the program and how to use them.

# Autocorrect

This program also has a built-in autocorrect tool. If you've just misspelled a word, hit Right Alt and the program will replace the text with the closest word match. This works in any window while PyTextStudio is running.

*This feature is not available in the .exe version of PyTextStudio.*

![Example of autocorrect in use](https://i.imgur.com/pHRwQFX.gif)

# Notes

If the user tries to save without first loading any existing data, the program will ask them if they want to overwrite their data or add the new expansions together with their old data. This helps to prevent any loss of data.

Similarly, if the user tries to load old expansions while they have active data they haven't saved yet, the program will ask if they want to load now (erasing any new expansions they haven't saved yet) or cancel loading.

The program can **crash on some systems** when the user loads data, then tries to use new text expansions that they've created after loading. To avoid this, save any expansions you've created after loading, restart the program, then load again. Alternatively, you can create text expansions before loading, then save and choose to add your expansions together.