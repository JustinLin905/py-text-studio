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
# v2.0.0 published in November 2020

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

# Lists to contain user's short words and the corresponding expanded text
short_words = []
expanded_words = []

# Hotkey variables, change these to change what keys activate text expansion and autocorrect
expansionHotkey = Key.ctrl_r
autocorrectHotkey = Key.alt_r






### FUNCTIONS ###

# Select last function, selects the last typed word using CTRL+SHIFT+LEFT, then copies it
def select_last():

    # Using pynput to simulate individual keys seems to be the only way to automate CTRL+SHIFT+LEFT properly
    keyControl.press(Key.ctrl)
    keyControl.press(Key.shift)
    keyControl.press(Key.left)

    keyControl.release(Key.ctrl)
    keyControl.release(Key.shift)
    keyControl.release(Key.left)

    # Copy the selection using pyautogui
    pyautogui.hotkey("ctrl", "c")





# Create new expansion function, used to add new text shortcuts and expansions 
def create_new_expansion():

    newShortWord = str(input("\nEnter a short word that you would like to expand: "))

    newExpandedWord = str(input("Enter the text that you want the short word to expand into: "))

    # Append user input into the lists that store words
    short_words.append(newShortWord)
    expanded_words.append(newExpandedWord)

    print ('\nText expansion registered! Type "{0}" and hit Right Control to expand it into "{1}".'.format(newShortWord, newExpandedWord))





# Function used to save shortcuts to a selected save file
def save_file():

    # Make the word lists global to access them in this function
    global short_words
    global expanded_words

    # Data match variable, used to check if save files contain potentially sensitive data from user
    dataMatch = 0

    # File size variable, used to check if save file is empty
    fileSize = 0

    # Loaded short words / expanded words lists, used to temporarily store loaded data from save file
    loaded_short_words = []
    loaded_expanded_words = []

    # Ask user which profile to save to
    profileChoice = str(input("\nWhere would you like to save? (file name without .txt): "))

    saveFileName = r"savefiles\{0}.txt".format(profileChoice)


    # First, check if the user is saving to a file which has matching short words compared to currect active short words.
    # If there are no matches, it means that they might overwrite sensitive data that they saved before. Ask user to confirm saving.
    # If there are several matches between the save file data and current data, or the selected file is empty, go straight to saving.

    # Check if the save file is empty. If the save file doesn't exist, the program will create the file then save to it
    try:

        fileSize = os.path.getsize(saveFileName)

        # Attempt loading from the selected file
        with open (saveFileName, "rb") as f:
                
            loaded_short_words, loaded_expanded_words = pickle.load(f)

        # Iterate through the current shortcuts and compare them to save data. If there is a match, increase dataMatch
        for i in range(len(short_words)):

            if short_words[i] == loaded_short_words[i]:

                dataMatch += 1

    # Catch exceptions to prevent crashes
    except FileNotFoundError:

        fileSize = 0

    except IndexError:

        fileSize = 0

    except EOFError:

        fileSize = 0

    

    # If matches make up less than half of data on save file, and file is not empty, ask user if they want to overwrite or add. 
    # This is to help prevent accidental overwriting.
    if dataMatch < len(loaded_short_words) / 2 and fileSize != 0:

        print ("\nATTENTION: It looks like you already have some expansions saved on this file from an earlier time.")
        print("Would you like to overwrite this save data with your current expansions, or add the current expansions along with your old ones?")

        while True:

            overwriteInput = str(input("\nOverwrite or add? (overwrite/add): "))


            # If the user chooses to overwrite their save data
            if overwriteInput == "overwrite":

                # Save current active expansions, overwriting any existing data
                with open (saveFileName, "wb") as f:

                    pickle.dump ([short_words, expanded_words], f)

                print ("\n\n----------------------------------------------------------------------------------------")

                print ('\nYour text expansions have been saved successfully. Type "load" to access them later.')

                print ("\nYour short words list:", short_words)
                print ("Your expanded words list:", expanded_words)

                print ("\n----------------------------------------------------------------------------------------")

                # Break this input loop
                break

            # If the user chooses to add their expansions on top of their save data
            elif overwriteInput == "add":

                # First, load the existing data
                with open (saveFileName, "rb") as f:

                    loaded_short_words, loaded_expanded_words = pickle.load(f)

                    # Combine current data and save data
                    short_words = short_words + loaded_short_words
                    expanded_words = expanded_words +loaded_expanded_words

                    # Remove any duplicates that may be in the lists from the combining process
                    short_words = list(dict.fromkeys(short_words))
                    expanded_words = list(dict.fromkeys(expanded_words))

                # Save all of the text expansions
                with open (saveFileName, "wb") as f:

                    pickle.dump ([short_words, expanded_words], f)

                print ("\n\n----------------------------------------------------------------------------------------")

                print ('\nYour text expansions have been saved successfully. Type "load" to access them later.')

                print ("\nYour short words list:", short_words)
                print ("Your expanded words list:", expanded_words)

                print ("\n----------------------------------------------------------------------------------------")

                # Break this input loop
                break

            else:

                print ("Invalid input, please try again.")



    # If save file is deemed safe, go straight to saving instead of asking for user input
    else:
        
        # Open save file and save current active expansions into file
        with open (saveFileName, "wb") as f:

            pickle.dump ([short_words, expanded_words], f)

        print ("\n\n----------------------------------------------------------------------------------------")

        print ('\nYour text expansions have been saved successfully. Type "load" to access them later.')

        print ("\nYour short words list:", short_words)
        print ("Your expanded words list:", expanded_words)

        print ("\n----------------------------------------------------------------------------------------")





# Function used to load shortcuts from a selected save file
def load_file():

    # Make the word lists global to access them in this function
    global short_words
    global expanded_words

    # Ask user which profile to load from. Ask again if input is not an existing save file
    while True:

        profileChoice = str(input("\nWhere would you like to load from? (file name without .txt): "))

        try:

            saveFileName = r"savefiles\{0}.txt".format(profileChoice)

            # Load from user choice using pickle
            with open (saveFileName, "rb") as f:
                    
                loaded_short_words, loaded_expanded_words = pickle.load(f)

            break

        except FileNotFoundError:

            print ("Oops! A save file of that name doesn't exist. Please try again.")

        
    # Set the active shortcuts and expansions to the ones just loaded
    short_words = loaded_short_words
    expanded_words = loaded_expanded_words

    print ("\n\n-----------------------------------------------------------------------")

    print ('\nYour text expansions have been loaded successfully.')

    print ("\nYour short words list:", short_words)
    print ("Your expanded words list:", expanded_words)

    print ("\n-----------------------------------------------------------------------")





# Text expansion function, used to expand shortcut words into their corresponding expanded text
def text_expansion ():

    # Store what was copied from the select_last function in variable selectedWord
    selectedWord = Tk().clipboard_get()

    # If the selected word is one of user's shortwords
    if selectedWord in short_words:

        # Find the index of the short word in the short_words list
        wordIndex = short_words.index(str(selectedWord))
        
        # Find the corresponding expanded text
        expanded = expanded_words[int(wordIndex)]

        # Sleep a little more to give more time to release right control
        sleep(0.05)

        # Automatically type out the expanded text
        pyautogui.typewrite(str(expanded))





# Autocorrect function, corrects the selected word into the closest word match using autocorrect
def autocorrect():

    # Store what was copied from the select_last function in variable selectedWord
    selectedWord = Tk().clipboard_get()

    # Autocorrect by finding most likely word match to selectedWord, then typewrite the corrected word using pyautogui
    correctedWord = spell(str(selectedWord))

    # Sleep a little longer to give user to time to release right alt key
    sleep(0.1)

    pyautogui.typewrite(correctedWord)





# On press function, uses the keyboard listener to run other functions if certain keys are pressed
def on_press(key):

    global short_words

    # If right control is pressed (the text expansion hotkey)
    if key == expansionHotkey:

        # Only run code below if there are active expansions
        if len(short_words) > 0:

            # Sleep for a brief period before running select last. This gives user time to release cntrl, which could cause unintended actions
            sleep(0.1)          

            select_last()
            text_expansion()

    # If right alt is pressed (the autocorrect hotkey)
    elif key == autocorrectHotkey:

        # Sleep for a brief period before running select last. This gives user time to release alt, which could cause unintended actions
        sleep (0.1)         
        
        select_last()
        autocorrect()   









### MAIN PROGRAM ###

# Start keyboard listener so program can detect when user presses expansion or autocorrect hotkeys
listener = Listener(
    on_press=on_press)
listener.start()

# Print intro text

print ("\n █▀█ █▄█ ▀█▀ █▀▀ ▀▄▀ ▀█▀ █▀ ▀█▀ █░█ █▀▄ █ █▀█  v2.0.0")
print (" █▀▀ ░█░ ░█░ ██▄ █░█ ░█░ ▄█ ░█░ █▄█ █▄▀ █ █▄█  .py")

print ("\n------------------------------------------------------")

print ("\nWelcome to PyTextStudio!")
print ("Remember to save regularly.")



# Main Loop
while running:

    userInput = str(input("\nWhat would you like to do? (new/save/load/help): "))

    if userInput == "new" or userInput == "save" or userInput == "load" or userInput == "help":

        # If user types in new, call the function to create a new text expansion
        if userInput == "new":

            create_new_expansion()

        # If user types in save, save their current text expansions using the save file function
        elif userInput == "save":

            save_file()

        # If user types in load, load text expansions using the load file function
        elif userInput == "load":

            load_file()

        # If user types in help, print help message
        else:

            print ("\n------------------------------------------------------------------------------")

            print ("\nPyTextStudio lets you make and save your own text expansions.")

            print ('\nType in "new" to create a new expansion. Type in a shortcut word, then assign it to some expanded text. \nYou can now convert the shortcut word into the expanded text by typing the short word, then \nhitting Right Control.')
            
            print ('\nE.x. if your shortcut text is "hw" and you assign the expanded text "Hello World!" to the shortcut, you can \ntype "hw" then hit Right Control. This program will automatically convert the shortword into "Hello World!". \nThis works in any window.')

            print ("\nThis program also has a built-in autocorrect tool. If you've misspelled your last typed word, \nhit Right Alt to autocorrect it to the closest word match.")

            print ('\nThere is a Save / Load feature for your expansions as well. \nType in "save" and choose a file name to save your current active text expansions. If a file of that name \ndoesn\'t already exist, the program will create it for you.')

            print ('Type "load" and choose a file name to use shortcuts that you have saved before.')

            print ("\n------------------------------------------------------------------------------")


    # Print error message upon invalid input
    else:

        print ("Invalid input, please try again.")
    


