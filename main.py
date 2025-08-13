import pyautogui
import time
import random

# Settings
TEXT = """This is the text that will be typed into Google Docs.
It can be multiple lines if you want. Add as much as you like."""
INITIAL_DELAY = 2  # seconds before starting typing
MIN_BREAK = 1      # minimum pause between words (seconds)
MAX_BREAK = 199    # maximum pause between words (seconds)
TYPING_SPEED = 0.02  # seconds per character

# Countdown so you can click into Google Docs
print(f"You have {INITIAL_DELAY} seconds to switch to Google Docs...")
time.sleep(INITIAL_DELAY)

# Split into words so pauses happen naturally
words = TEXT.split()

for i, word in enumerate(words):
    pyautogui.typewrite(word, interval=TYPING_SPEED)  # type the word
    if i < len(words) - 1:
        pyautogui.typewrite(" ", interval=TYPING_SPEED)  # add space
        pause_time = random.randint(MIN_BREAK, MAX_BREAK)
        print(f"[Pause for {pause_time} seconds]")
        time.sleep(pause_time)
