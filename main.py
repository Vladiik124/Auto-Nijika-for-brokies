#import packages
import psutil #check process
import pydirectinput #set cursor
from win32api import GetSystemMetrics #get screen res
import time #sleep
import keyboard #detecting key presses

#title
print("BOKKI THE ROCK AUTO NIJIKA FOR BROKIES\nSpam F to stop\npress enter to start")
input()

def is_process_running(process_name):
    for process in psutil.process_iter():
        if (process.name() == process_name):
            return True
    return False

def get_screen_info():
    return GetSystemMetrics(0),GetSystemMetrics(1)

def moveTo(NewX, NewY, step):
    x, y = pydirectinput.position()

    stepX = (NewX - x) / step
    stepY = (NewY - y) / step

    for i in range(step):
        x += stepX
        y += stepY
        pydirectinput.moveTo(int(x), int(y))
        time.sleep(0.001)  # Smooth movement delay

    pydirectinput.moveTo(NewX, NewY)  # Ensure final position is accurate


#Check if roblox process is open
if (is_process_running("RobloxPlayerBeta.exe")):
        #Check screen resolutionf
        print(f"screen size {get_screen_info()}")
        #ask when player is sur


        #depending on screen res, automate.
        width, height = get_screen_info()
        print("if u are sure u want to do this press enter, otherwise close or smth idk (¬‿¬)")
        input()

        #AWESOME COUNTDOWN!!!!!!
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        moveTo(int(width / 2), int(height / 2), 10)
        time.sleep(1)
        print("skid")

        x=True
        while(not keyboard.is_pressed('f')):
            moveTo(int(width/2), int(height-200),1)
            pydirectinput.click()
            moveTo(int(width/2), int(height/2+250), 1)
            pydirectinput.click()

else:
     print("roblox not open! try again")