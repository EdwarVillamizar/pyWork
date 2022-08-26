import pyautogui
import time
from os import mkdir, stat
from datetime import datetime

now = str(datetime.now().strftime('%d-%m-%Y'))

while True:
    
    try:
        stat(now)
    except:
        mkdir(now)

    name = str(datetime.now().strftime('Time %H.%M.%S'))

    pyautogui.screenshot().save(now +'/'+ name +'.png')

    print('File '+name+' is ok.')

    time.sleep(120)