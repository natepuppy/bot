import pyautogui as bot
import time
import random as random_number
import math
from pyclick import HumanClicker
import win32clipboard     # pip install pywin32
import pandas as pd
import csv

hc = HumanClicker()

def track_mouse(num):
  for i in range(num):
    time.sleep(5.0)
    print(bot.position())

def click_picture(picture_path, wait = 0.0, click = True):
  time.sleep(wait)
  result = bot.locateCenterOnScreen(picture_path)
  if result == None:
    print('not found')
    return False
  hc.move((result[0], result[1]))
  if click:
    hc.click()
  return True

# def move_to_picture(picture_path, wait = 0.0):
#   time.sleep(wait)
#   result = bot.locateCenterOnScreen(picture_path)
#   if result == None:
#     print('not found')
#     return False
#   hc.move((result[0], result[1]))
#   return True

def verify_you_are_human():
  # click_picture('pictures/claim_rewards.PNG', 0.2)
  click_picture('pictures/learn_more.PNG', 0.2)
  click_picture('pictures/claim.PNG', 1.0)

  time.sleep(1.5)

  if click_picture('pictures/circle_text.PNG', click=False):
    print("circle")
    x, y = bot.locateCenterOnScreen('pictures/circle.PNG')
    click_picture('pictures/brave_logo.PNG', 0.2, click=False)
    bot.mouseDown()
    hc.move((x, y), 5)
    bot.mouseUp()

  elif click_picture('pictures/triangle_text.PNG', click=False):
    print("triangle")
    x, y = bot.locateCenterOnScreen('pictures/triangle.PNG')
    click_picture('pictures/brave_logo.PNG', 0.2, click=False)
    bot.mouseDown()
    hc.move((x, y), 5)
    bot.mouseUp()

  elif click_picture('pictures/square_text.PNG', click=False):
    print("square")
    x, y = bot.locateCenterOnScreen('pictures/square.PNG')
    click_picture('pictures/brave_logo.PNG', 0.2, click=False)
    bot.mouseDown()
    hc.move((x, y), 5)
    bot.mouseUp()






def kill_file_explorer():
  # change UAC settings -- https://superuser.com/questions/1435771/windows-10-how-do-i-always-allow-an-app-to-make-changes
  import win32com.shell.shell as shell
  kill = 'taskkill /f /im explorer.exe && start explorer.exe' 
  shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+kill)


# def run_verification(start, stop):
#   cmd = 'taskkill /IM "explorer.exe" /F' 
#   refresh_range_x = (72,97)
#   refresh_range_y = (35,58)

#   while(True):
#     for i in range(start, stop):

#       if i % 50 == 0:
#         kill_file_explorer()

#       print("user", i)
#       launch_as_different_user('user' + str(i))
#       time.sleep(.5)
#       close_default_browser()
#       fresh_tab()
            
#       close_window()

#     # append_csv(to_float_list(amount_of_bat))
#   time.sleep(2)




time.sleep(5)
verify_you_are_human()
