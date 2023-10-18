import tkinter as tk
from tkinter import messagebox
import random
import time

# Define some constants
MAX_ERRORS = 5 # Maximum number of errors allowed
TIME_LIMIT = 60 # Time limit in seconds
WORDS_FILE = "words.txt" # File name of the words list

# Load the words from the file
with open(WORDS_FILE) as f:
    words = f.read().splitlines()

# Shuffle the words randomly
random.shuffle(words)

# Initialize some variables
word_index = 0 # Index of the current word
char_index = 0 # Index of the current character
typed = "" # Characters typed so far
errors = 0 # Number of errors made
start_time = time.time() # Start time of the test
end_time = 0 # End time of the test
running = True # Flag to indicate if the test is running

# Create a root window
root = tk.Tk()
root.title("Typing Speed Test")

# Create a label to display the instructions
instructions = tk.Label(root, text="Type this: (press ENTER when you are ready)")
instructions.pack()

# Create a label to display the current word
word_label = tk.Label(root, text=words[word_index], font=("Courier", 24))
word_label.pack()

# Create an entry to get the user input
entry = tk.Entry(root, font=("Courier", 24))
entry.pack()

# Create a label to display the time and errors
info_label = tk.Label(root, text=f"Time: {int(time.time() - start_time)} / {TIME_LIMIT} s\nErrors: {errors} / {MAX_ERRORS}")
info_label.pack()

# Define a function to handle the key press event
def key_press(event):
    global word_index, char_index, typed, errors, start_time, end_time, running

    # Get the key pressed by the user
    key = event.char

    # Check if the key is valid (a letter or a space)
    if key in "abcdefghijklmnopqrstuvwxyz ":
        # Get the current word and character
        word = words[word_index]
        char = word[char_index]

        # Check if the character matches the expected one
        if key == char:
            # Append the character to the typed string
            typed += key

            # Increment the character index
            char_index += 1

            # Check if the whole word is typed correctly
            if char_index == len(word):
                # Increment the word index and reset the character index and typed string
                word_index += 1
                char_index = 0
                typed = ""

                # Check if all words are typed correctly
                if word_index == len(words):
                    # Stop the test and record the end time
                    running = False
                    end_time = time.time()
        else:
            # Increment the errors and check if they exceed the maximum limit
            errors += 1
            if errors > MAX_ERRORS:
                # Stop the test and record the end time
                running = False
                end_time = time.time()

        # Update the labels with the new values
        word_label.config(text=word[:char_index] + word[char_index:].upper())
        info_label.config(text=f"Time: {int(time.time() - start_time)} / {TIME_LIMIT} s\nErrors: {errors} / {MAX_ERRORS}")

    # Check if the key is ENTER and the test is not running yet
    elif key == "\r" and not running:
        # Start the test and reset some variables
        running = True
        start_time = time.time()
        end_time = 0

        # Update the labels with the new values
        word_label.config(text=words[word_index])
        info_label.config(text=f"Time: {int(time.time() - start_time)} / {TIME_LIMIT} s\nErrors: {errors} / {MAX_ERRORS}")

# Bind the key press event to the entry widget
entry.bind("<Key>", key_press)

# Define a function to update the timer every second
def update_timer():
    global running, end_time

    # Check if the test is running and not finished yet
    if running and time.time() - start_time < TIME_LIMIT:
        # Update the time label with the new value
        info_label.config(text=f"Time: {int(time.time() - start_time)} / {TIME_LIMIT} s\nErrors: {errors} / {MAX_ERRORS}")

        # Schedule another call to this function after one second
        root.after(1000, update_timer)
    else:
        # Stop the test and record the end time if not already done
        if running:
            running = False
            end_time = time.time()

        # Calculate the words per minute and the accuracy
        wpm = round(word_index * 60 / (end_time - start_time), 2)
        accuracy = round(100 - errors * 100 / (word_index + 1), 2)

        # Display the results in a message box
        messagebox.showinfo("Results", f"Your typing speed was {wpm} words per minute with {accuracy}% accuracy.")

# Call the update timer function for the first time
update_timer()

# Start the main loop of the window
root.mainloop()
