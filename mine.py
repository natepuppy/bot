import pyautogui as bot
import time
import random as random_number
import math
from pyclick import HumanClicker
import win32clipboard     # pip install pywin32
import pandas as pd
import csv
import win32com.shell.shell as shell




hc = HumanClicker()

def random(start, stop):
  num = random_number.uniform(start, stop)
  return num


def move_to_random_spot(pixel_range_x = (200, 1720), pixel_range_y = (200, 880), start_time = .05, stop_time = 0.1): 
  x = math.floor(random(pixel_range_x[0], pixel_range_x[1]))
  y = math.floor(random(pixel_range_y[0], pixel_range_y[1]))
  hc.move((x, y),random(start_time, stop_time))
  

def close_window():
    close_window = (1894, 14)
    hc.move((close_window),random(0.05, 0.1))
    hc.click()


def full_screen():
  bot.keyDown('alt')
  time.sleep(random(.05, .1))
  bot.keyDown('space')
  time.sleep(random(.05, .1))
  bot.keyDown('x')
  time.sleep(random(.05, .1))

  bot.keyUp('alt')
  time.sleep(random(.05, .1))
  bot.keyUp('space')
  time.sleep(random(.05, .1))
  bot.keyUp('x')
  time.sleep(random(.05, .1))


def launch_as_different_user(user):
  time.sleep(.11)     # add moretime here to close all apps
  brave_app = (33, 31)
  run_as_different_user = (116, 151)
  password = '0223'

  bot.keyDown('shift')
  bot.rightClick(brave_app)
  time.sleep(0.5)
  bot.click(run_as_different_user)
  time.sleep(0.5)
  bot.keyUp('shift')
  time.sleep(0.5)
  bot.write(user)
  time.sleep(0.5)
  bot.press('tab') 
  time.sleep(0.5)
  bot.write(password)
  time.sleep(0.5)
  bot.keyDown('enter')
  time.sleep(0.5)
  bot.keyUp('enter')
  time.sleep(.1)

  full_screen()
  # time.sleep(0.5)

def hotkey(key_arr, time_lower_bound = 0.1, time_upper_bound = 0.11):
  time.sleep(random(time_lower_bound, time_upper_bound))

  for i in range(len(key_arr)):
    time.sleep(random(time_lower_bound, time_upper_bound))
    bot.keyDown(key_arr[i])

  for i in reversed(range(len(key_arr))):
    time.sleep(random(time_lower_bound, time_upper_bound))
    bot.keyUp(key_arr[i])

  time.sleep(random(time_lower_bound, time_upper_bound))

def close_default_browser():
    # set_as_default = (950, 255)
    not_now = (1066, 254)
    hc.move((not_now),random(0.05, 0.1))
    hc.click()


def key_press(key, time_lower_bound = 0.1, time_upper_bound = 0.11):
  length_of_press = random(time_lower_bound, time_upper_bound)

  bot.keyDown(key)
  time.sleep(length_of_press)
  bot.keyUp(key)

def type_string(string):
  for i in range(len(string)):
    key_press(string[i])


def fresh_tab():
  time.sleep(0.3)
  hotkey(['ctrl', 't'])
  close_tab()

def close_tab():
  close_tab = (229, 12)
  hc.move((close_tab),random(1.5, 2.3))
  hc.click()


def click_picture(picture_path, wait = 0.0, click = True):
  time.sleep(wait)
  result = bot.locateCenterOnScreen(picture_path, confidence = .9)
  if result == None:
    print('not found')
    return False
  hc.move((result[0], result[1]), random(.1, .2)) 
  if click:
    hc.click()
  return True


def open_rewards_tab():
    url = 'brave://rewards/'
    fresh_tab()
    bot.write(url)
    bot.press('enter')


# def click_picture(picture_path, wait = 0.0, click = True):
#   time.sleep(wait)
#   result = bot.locateCenterOnScreen(picture_path, confidence = .9)
#   if result == None:
#     print('not found')
#     return False
#   hc.move((result[0], result[1]), random(.1, .2)) 
#   if click:
#     hc.click()
#   return True

def verify_you_are_human():

  open_rewards_tab()

  time.sleep(1)

  picture_path = 'pictures/claim.PNG'
  picture_path_2 = 'pictures/almost_there.PNG'
  if not click_picture(picture_path, wait = 0.0, click = True) and not click_picture(picture_path, wait = 0.0, click = False):
    return

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

    time.sleep(1)
  
  verify_you_are_human()

def kill_file_explorer():
  # change UAC settings -- https://superuser.com/questions/1435771/windows-10-how-do-i-always-allow-an-app-to-make-changes
  import win32com.shell.shell as shell
  kill = 'taskkill /f /im explorer.exe && start explorer.exe' 
  shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+kill)


def mine(start, stop, number_refreshes=15):
  cmd = 'taskkill /IM "explorer.exe" /F' 
  refresh_range_x = (72,97)
  refresh_range_y = (35,58)

  while(True):
    for i in range(start, stop):

      if i % 50 == 0:
        kill_file_explorer()

      print("user", i)
      launch_as_different_user('user' + str(i))
      time.sleep(.4)
      close_default_browser()


      fresh_tab()
      # verify_you_are_human()

      for j in range(number_refreshes):
        move_to_random_spot(pixel_range_x = refresh_range_x, pixel_range_y = refresh_range_y, start_time = 0.01, stop_time = 0.1)
        hc.click()

        move_to_random_spot(start_time = 0.01, stop_time = 0.1)
            
      close_window()

    # append_csv(to_float_list(amount_of_bat))
  time.sleep(2)


bot.FAILSAFE_POINTS = [(0, 1079)]
hc.FAILSAFE_POINTS = [(0, 1079)]

start = 1

stop = 1000

number_refreshes = 20

mine(start, stop, number_refreshes) 


# def runas():
#   print("werw")
#   # change UAC settings -- https://superuser.com/questions/1435771/windows-10-how-do-i-always-allow-an-app-to-make-changes
#   import win32com.shell.shell as shell
#   cmd = 'echo "0223" | runas /user:user10 "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"' 
#   # cmd = 'diuaskdjn' 
#   shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+cmd)
#   print("4")

# runas()


# runas /user:user567 "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# def track_mouse():
#   for i in range(10):
#     time.sleep(5.0)
#     print(bot.position())
# track_mouse()




# cmd = 'taskkill /IM "explorer.exe" /F' 
# shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+cmd)

# def track_mouse():
#   for i in range(10):
#     time.sleep(5.0)
#     print(bot.position())

# track_mouse()


# taskkill /f /im explorer.exe
# start explorer.exe
