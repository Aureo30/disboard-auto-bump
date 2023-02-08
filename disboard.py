import pynput
import time
from pynput.keyboard import Key, Controller
text = "/bump"

keyboard = Controller()
while True:
        # écris /bump
        keyboard.type(text)
        # attends 2 seconde
        time.sleep(2)
        # appuie sur entrée pour sléctionner la commande
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # appuie sur entrée pour envoyer la commande
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # attend deux heures
        time.sleep(7200)