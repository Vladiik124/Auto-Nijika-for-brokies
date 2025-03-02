#import packages
import psutil #check process
import pydirectinput #set cursor
from win32api import GetSystemMetrics #get screen res
import time #sleep
import keyboard #detecting key presses

#title
print("BOKKI THE ROCK AUTO NIJIKA FOR BROKIES\npress enter to start")
input()

def is_process_running(process_name):
    for process in psutil.process_iter():
        if (process.name() == process_name):
            return True
    return False

def get_screen_info():
    return GetSystemMetrics(0),GetSystemMetrics(1)


#Check if roblox process is open
if (is_process_running("RobloxPlayerBeta.exe")):
        #Check screen resolution
        print(f"screen size {get_screen_info()}")
        #ask when player is sure


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
        pydirectinput.moveTo(int(width / 2), int(height / 2), duration=4)
        time.sleep(1)
        print("skid")

        x=True
        while(x):
            if (keyboard.is_pressed('f')):
                x=False
            pydirectinput.moveTo(int(width/2), int(height-200))
            pydirectinput.click()
            pydirectinput.moveTo(int(width/2), int(height/2+350))
            pydirectinput.click()

else:
     print("roblox not open! try again")



