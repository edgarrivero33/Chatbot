import os

try:
    os.system('cmd /k "rasa shell"')
except:
    print('could not start the bot')