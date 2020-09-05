######################################################################

# PyTextStudio.py  :  a minimal script which allows users to  
# use, save, and load their own custom text expansions.

# Dependencies: pyautogui, pynput, autocorrect

# The default configuration for hotkeys are:

# Right Control to expand last typed word
# Right Alt to autocorrect last typed word
 
# Feel free to reuse, edit, or transform this script into
# whatever you like!

# Written by Justin Lin in August 2020

######################################################################



import pyautogui
from pynput.keyboard import Key, Controller, Listener
from autocorrect import Speller
from time import sleep
from tkinter import Tk
import pickle
import os


# Assign pynput controller to 'keyControl'
keyControl = Controller()

# Assign autocorrect Speller() to spell
spell = Speller()

# Main running variable
running = True

# Recently loaded bool, controls warnings to protect user save data
recentlyLoaded = False

# Lists to contain user's short words and the corresponding expanded text
short_words = []
expanded_words = []

# Hotkey variables, change these to change what keys activate text expansion and autocorrect
expansionHotkey = Key.ctrl_r
autocorrectHotkey = Key.alt_r



### FUNCTIONS ###

# Select last function, selects the last typed word using CTRL+SHIFT+LEFT, then copies it
def selectLast():

    # Using pynput seems to be the only way to automate CTRL+SHIFT+LEFT properly
    keyControl.press(Key.ctrl)
    keyControl.press(Key.shift)
    keyControl.press(Key.left)

    keyControl.release(Key.ctrl)
    keyControl.release(Key.shift)
    keyControl.release(Key.left)

    # Copy the selection using pyautogui
    pyautogui.hotkey("ctrl", "c")


# Create new expansion function, used to add new text shortcuts and expansions 
def createNewExpansion():

    newShortWord = str(input("\nEnter a short word that you would like to expand: "))

    newExpandedWord = str(input("Enter the text that you want the short word to expand into: "))

    # Append user input into the lists that store words
    short_words.append(newShortWord)
    expanded_words.append(newExpandedWord)

    print ('\nText expansion registered! Type "{0}" and hit Right Control to expand it into "{1}".'.format(newShortWord, newExpandedWord))




# Function used to save shortcuts to userShortcuts.txt
def saveFile():

    # Make the word lists global to access them in this function
    global short_words
    global expanded_words
    global recentlyLoaded

    # Check if the save file is empty
    fileSize = os.path.getsize("userShortcuts.txt")

    # If the save file is empty or the user has loaded recently, go straight to saving
    if fileSize == 0 or recentlyLoaded == True:

        with open ("userShortcuts.txt", "wb") as f:

            pickle.dump ([short_words, expanded_words], f)

            print ("\n\n#######################################################################################")

            print ('\nYour text expansions have been saved successfully. Type "load" to access them later.')

            print ("\nYour short words list:", short_words)
            print ("Your expanded words list:", expanded_words)

            print ("\n########################################################################################")

    # If the save file has data that may be overwritten, warn the user
    else:

        print ("\nATTENTION: It looks like you already have some text expansions saved from an earlier time.")
        print("Would you like to overwrite this save data with your current expansions, or add the current expansions together with your old ones?")

        while True:

            overwriteInput = str(input("\nOverwrite or add? (overwrite/add): "))

            if overwriteInput == "overwrite" or overwriteInput == "add":

                # If the user chooses to overwrite their save data
                if overwriteInput == "overwrite":

                    # Save current active expansions, overwriting any existing data
                    with open ("userShortcuts.txt", "wb") as f:

                        pickle.dump ([short_words, expanded_words], f)

                        print ("\n\n#######################################################################################")

                        print ('\nYour text expansions have been saved successfully. Type "load" to access them later.')

                        print ("\nYour short words list:", short_words)
                        print ("Your expanded words list:", expanded_words)

                        print ("\n########################################################################################")

                        # Set this to true, since data was overwritten during this process
                        recentlyLoaded = True

                        # Break this input loop
                        break

                # If the user chooses to add their expansions on top of their save data
                else:

                    # First, load the existing data
                    with open ("userShortcuts.txt", "rb") as f:

                        loaded_short_words, loaded_expanded_words = pickle.load(f)

                        # Combine current data and save data
                        short_words = short_words + loaded_short_words
                        expanded_words = expanded_words +loaded_expanded_words

                        # Remove any duplicates that may be in the lists from the combining process
                        short_words = list(dict.fromkeys(short_words))
                        expanded_words = list(dict.fromkeys(expanded_words))

                    # Save all of the text expansions
                    with open ("userShortcuts.txt", "wb") as f:

                        pickle.dump ([short_words, expanded_words], f)

                        # Return success message
                        print ("\n\n#######################################################################################")

                        print ('\nYour text expansions have been saved successfully. Type "load" to access them later.')

                        print ("\nYour short words list:", short_words)
                        print ("Your expanded words list:", expanded_words)

                        print ("\n########################################################################################")

                        # Set this to true, since data was loaded during this process
                        recentlyLoaded = True

                        # Break this input loop
                        break

            else:

                print ("Invalid input, please try again.")




# Function used to load shortcuts from userShortcuts.txt
def loadFile():

    global short_words
    global expanded_words
    global recentlyLoaded

    # Check if the save file is empty
    fileSize = os.path.getsize("userShortcuts.txt")

    if fileSize != 0:

        with open ("userShortcuts.txt", "rb") as f:

            loaded_short_words, loaded_expanded_words = pickle.load(f)

            # Check if there are any new expansions that were created this session that don't match the load data
            if len(short_words) != 0 and short_words != loaded_short_words:

                print ("\nATTENTION: Loading now will overwrite any new shortcuts that you haven't saved yet.")

                while True:

                    loadInput = str(input("Proceed? (yes/no): "))

                    if loadInput == "yes" or loadInput == "no":

                        if loadInput == "yes":

                            short_words = loaded_short_words
                            expanded_words = loaded_expanded_words

                            print ("\n\n###################################################################")

                            print ('\nYour text expansions have been loaded successfully.')

                            print ("\nYour short words list:", short_words)
                            print ("Your expanded words list:", expanded_words)

                            print ("\n###################################################################")


                            # Set recently loaded to true, so data overwrite warning won't show the next time user tries to save
                            recentlyLoaded = True

                            # Break this input loop
                            break

                        else:

                            # Break this input loop
                            break

                    else:

                        print ("Invalid input, please try again.")


            # If it is safe to load, go straight to loading data
            else:

                short_words = loaded_short_words
                expanded_words = loaded_expanded_words

                print ("\n\n###################################################################")

                print ('\nYour text expansions have been loaded successfully.')

                print ("\nYour short words list:", short_words)
                print ("Your expanded words list:", expanded_words)

                print ("\n###################################################################")

                # Set recently loaded to true, so data overwrite warning won't show the next time user tries to save
                recentlyLoaded = True


    else:

        print ("The save file is empty, there is nothing to load!")



# Text expansion function, used to expand shortcut words into their corresponding expanded text
def textExpansion ():

    # Store what was copied from the selectLast function in variable selectedWord
    selectedWord = Tk().clipboard_get()

    # If the selected word is one of user's shortwords
    if selectedWord in short_words:

        # Find the index of the short word in the short_words list
        wordIndex = short_words.index(str(selectedWord))
        
        # Find the corresponding expanded text
        expanded = expanded_words[int(wordIndex)]

        # Sleep a little more to give more time to release right enter
        sleep(0.05)

        # Automatically type out the expanded text
        pyautogui.typewrite(str(expanded))



# Autocorrect function, corrects the selected word into the closest word match using autocorrect
def autocorrect():

    # Store what was copied from the selectLast function in variable selectedWord
    selectedWord = Tk().clipboard_get()

    # Autocorrect by finding most likely word match to selectedWord, then typewrite the corrected word using pyautogui
    correctedWord = spell(str(selectedWord))

    sleep(0.1)             # Sleep a little longer to give user to time to release right alt key

    pyautogui.typewrite(correctedWord)



# On press function, uses the keyboard listener to run other functions if certain keys are pressed
def on_press(key):

    global short_words

    # If right control is pressed (the text expansion hotkey)
    if key == expansionHotkey:

        # Only run code below if there are active expansions
        if len(short_words) > 0:

            sleep(0.1)          # Sleep for a brief period before running select last. This gives user time to release cntrl, which could cause unintended actions

            selectLast()
            textExpansion()

    # If right alt is pressed (the autocorrect hotkey)
    elif key == autocorrectHotkey:

        sleep (0.1)         # Sleep for a brief period before running select last. This gives user time to release alt, which could cause unintended actions
        
        selectLast()
        autocorrect()   









### MAIN PROGRAM ###

# Start keyboard listener
listener = Listener(
    on_press=on_press)
listener.start()


print ("\nWelcome to PyTextStudio!")


while running:

    userInput = str(input("\nWhat would you like to do? (new/save/load/help): "))

    if userInput == "new" or userInput == "save" or userInput == "load" or userInput == "help":

        # If user types in new, call the function to create a new text expansion
        if userInput == "new":

            createNewExpansion()

        # If user types in save, save their current text expansions using the save file function
        elif userInput == "save":

            saveFile()

        # If user types in load, load text expansions using the load file function
        elif userInput == "load":

            loadFile()

        # If user types in help, print help message
        else:

            print ("\nPyTextStudio lets you make and save your own text expansions.")

            print ('\nType in "new" to create a new expansion. Type in a shortcut word, then assign it to some expanded text. \nYou can now convert the shortcut word into the expanded text by typing the short word, then \nhitting Right Control.')
            
            print ('\nE.x. if your shortcut text is "hw" and you assign the expanded text "Hello World!" to the shortcut, you can \ntype "hw" then hit Right Control. This program will automatically convert the shortword into "Hello World!". \nThis works in any window.')

            print ("\nThis program also has a built-in autocorrect tool. If you've misspelled your last typed word, \nhit Right Alt to autocorrect it to the closest word match.")

            print ('\nThere is also a Save / Load feature. \nType in "save" to save your current active text expansions, or type "load" to use shortcuts that you \nhave saved before.')


    # Print error message upon invalid input
    else:

        print ("Invalid input, please try again.")
    


