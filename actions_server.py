import os

try:
    os.system('cmd /k "rasa run actions"')
except:
    print('could not start the time server')