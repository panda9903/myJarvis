import pyautogui
import os
import time
import webbrowser

song = "Im so sorry Imagine Dragons"

try:
    os.open('spotify')
    time.sleep(5)
    pyautogui.hotkey('Ctrl', 'l')
    pyautogui.write(song, interval=0.1)

    for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
        time.sleep(2)
        pyautogui.press(key)
except:
    webbrowser.open('https://open.spotify.com/search/' + song)
    time.sleep(5)
    pyautogui.click(x=700, y=400)
    time.sleep(3)
    pyautogui.click(x=600, y=600)
