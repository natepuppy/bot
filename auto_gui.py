import pyautogui as bot
import time
import random as random_number
import math
from pyclick import HumanClicker
import win32clipboard     # pip install pywin32
import pandas as pd
import csv

hc = HumanClicker()

 




def random(start, stop):
  num = random_number.uniform(start, stop)
  return num


def move_to_random_spot(pixel_range_x = (0, 1917), pixel_range_y = (0, 00), start_time = 1.5, stop_time = 2.3): 
  x = math.floor(random(pixel_range_x[0], pixel_range_x[1]))
  y = math.floor(random(pixel_range_y[0], pixel_range_y[1]))
  hc.move((x, y),random(start_time, stop_time))
  

def full_screen():
  # hotkey(['alt', 'space', 'x'])
  bot.keyDown('alt')
  time.sleep(random(.1, .3))
  bot.keyDown('space')
  time.sleep(random(.1, .3))
  bot.keyDown('x')
  time.sleep(random(.1, .3))

  bot.keyUp('alt')
  time.sleep(random(.1, .3))
  bot.keyUp('space')
  time.sleep(random(.1, .3))
  bot.keyUp('x')
  time.sleep(random(.1, .3))

def track_mouse():
  for i in range(10):
    time.sleep(5.0)
    print(bot.position())

def launch_as_different_user(user):
  print(user)

  time.sleep(0.5)     # add moretime here to close all apps
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
  time.sleep(1.5)

  full_screen()
  time.sleep(0.5)



    



def mouse_click(time_lower_bound = 0.1, time_upper_bound = 0.2):
  length_of_click = random(time_lower_bound, time_upper_bound)

  bot.mouseDown()
  time.sleep(length_of_click)
  bot.mouseUp()

def key_press(key, time_lower_bound = 0.1, time_upper_bound = 0.11):
  length_of_press = random(time_lower_bound, time_upper_bound)

  bot.keyDown(key)
  time.sleep(length_of_press)
  bot.keyUp(key)

def type_string(string):
  for i in range(len(string)):
    key_press(string[i])

def hotkey(key_arr, time_lower_bound = 0.1, time_upper_bound = 0.11):
  time.sleep(random(time_lower_bound, time_upper_bound))

  for i in range(len(key_arr)):
    time.sleep(random(time_lower_bound, time_upper_bound))
    bot.keyDown(key_arr[i])

  for i in reversed(range(len(key_arr))):
    time.sleep(random(time_lower_bound, time_upper_bound))
    bot.keyUp(key_arr[i])

  time.sleep(random(time_lower_bound, time_upper_bound))

def setup_monthly_contributions(url):
  search_bar = (562, 50)
  tip_menu = (1485, 49)
  send_a_tip = (1300, 383)
  bat_1 = (1617, 290)
  bat_5 = (1719, 288)
  bat_10 = (1820, 289)
  monthly_contribution = (1793, 151)
  set_monthly_contribution = (1717, 478)

  hc.move((search_bar),random(0.1, 0.5))
  mouse_click()
  hotkey(['ctrl', 'a'])
  key_press('backspace')
  type_string(url)
  key_press('enter')

  hc.move((tip_menu),random(1.3, 1.5))
  mouse_click()

  hc.move((send_a_tip),random(2.3, 2.5))
  mouse_click()

  hc.move((bat_1),random(1.3, 1.5))
  mouse_click()

  hc.move((monthly_contribution),random(1.3, 1.5))
  mouse_click()

  hc.move((set_monthly_contribution),random(1.3, 1.5))
  mouse_click()

def setup_auto_contribute(url):
  search_bar = (562, 50)
  tip_menu = (1481, 49)   
  include_in_auto_contribute_toggle = (1451, 350)

  hc.move((search_bar),random(1.5, 2.3))
  mouse_click()
  hotkey(['ctrl', 'a'])
  key_press('backspace')
  type_string(url)
  key_press('enter')

  hc.move((tip_menu),random(1.5, 2.3))
  mouse_click()

  time.sleep(.5)

  hc.move((include_in_auto_contribute_toggle),random(1.5, 2.3))
  mouse_click()


def browser_setup(start, stop):
  skip_tour = (783, 658)
  start_using_rewards = (1741, 539)
  start_using_rewards_2 = (1743, 542)
  start_using_rewards_3 = u(1737, 542)
  start_using_rewards_4 = (1743, 536)
  start_using_rewards_5 = (1743, 536)
  close_window = (1894, 14)

  for i in range(start, stop):
    launch_as_different_user('user' + str(i))

    # close_set_default_browser_popup()

    time.sleep(0.5)
    hc.move((skip_tour),random(1.5, 2.3))
    hc.click()

    time.sleep(1.5)
    hc.move((start_using_rewards),random(1.5, 2.3))
    hc.click()
    hc.move((start_using_rewards_2),random(1.5, 2.3))
    time.sleep(1.5)
    hc.move((start_using_rewards_3),random(1.5, 2.3))
    hc.click()
    time.sleep(1.5)
    hc.move((start_using_rewards_4),random(1.5, 2.3))
    hc.click()
    time.sleep(0.5)
    hc.move((start_using_rewards_5),random(1.5, 2.3))
    hc.click()
    time.sleep(1.5)
    hc.move((close_window),random(1.5, 2.3))
    mouse_click()
    time.sleep(0.5)


def setup_contributions(start, stop, url, monthly_contributions = True, auto_contribute = False):
  close_window = (1894, 14)

  for i in range(start, stop):
    launch_as_different_user('user' + str(i))
    time.sleep(2)
    not_now_default_browser_popup()
    fresh_tab()


    if monthly_contributions:
      setup_monthly_contributions(url)
    if auto_contribute:
      setup_auto_contribute(url)
    close_tab()

    hc.move((close_window),random(0.1, 2.3))
    mouse_click()
    time.sleep(.4)



def close_all_windows():
  bot.moveTo(1894, 14)
  bot.click()
  time.sleep(.2)  
  bot.click()
  time.sleep(.2)  
  bot.click()
  time.sleep(.2)  
  bot.click()
  time.sleep(.2)  

def close_tab():
  close_tab = (229, 12)
  hc.move((close_tab),random(1.5, 2.3))
  mouse_click()
  

def close_set_default_browser_popup():
  # Not Now
  # Point(x=1037, y=224)
  # Point(x=1114, y=243)
  default_range_x = (921,1001)
  default_range_y = (222,248)
  move_to_random_spot(pixel_range_x = default_range_x, pixel_range_y = default_range_y)
  mouse_click()

  close_settings_range_x = (1877,1915)
  close_settings_range_y = (3,26)
  move_to_random_spot(pixel_range_x = close_settings_range_x, pixel_range_y = close_settings_range_y)
  mouse_click()

def not_now_default_browser_popup():
  default_range_x = (1037,1114)
  default_range_y = (224,243)
  move_to_random_spot(pixel_range_x = default_range_x, pixel_range_y = default_range_y)
  mouse_click()
  time.sleep(0.5)
  skip_tour = (783, 658)
  
  # hc.move((skip_tour),random(0.1, 0.3))
  # mouse_click()
  # time.sleep(0.5)
  
  start_using_rewards = (1741, 539)
  hc.move((start_using_rewards),random(0.2, 0.3))
  mouse_click()



def fresh_tab():
  time.sleep(0.3)
  hotkey(['ctrl', 't'])
  close_tab()


def mine(start, stop, number_refreshes=15):
  # refresh = (83, 41)
  close_window = (1894, 14)
  refresh_range_x = (72,97)
  refresh_range_y = (35,58)
  amount_of_bat = []

  while(True):
    for i in range(start, stop):
      amount_of_bat = []
      launch_as_different_user('user' + str(i))
      time.sleep(2)
      not_now_default_browser_popup()
      fresh_tab()

      for j in range(number_refreshes):
        move_to_random_spot(pixel_range_x = refresh_range_x, pixel_range_y = refresh_range_y, start_time = 0.4, stop_time = 0.7)
        mouse_click()

        move_to_random_spot(start_time = 0.4, stop_time = 0.7)
        time.sleep(0.1)
      
     # amount_of_bat.append(get_amount_of_bat())
      
      hc.move((close_window),random(1.5, 2.3))
      mouse_click()

    append_csv(to_float_list(amount_of_bat))
  time.sleep(2)


def to_float_list(list_of_strings):
  float_map = map(float, list_of_strings)
  float_list = list(float_map)
  sum_num = sum(float_list)
  float_list.insert(0, sum_num)
  return float_list

def create_csv():
  filename = "record.csv"
  # opening the file with w+ mode truncates the file
  f = open(filename, "w+")
  f.close()

def append_csv(data):
  with open('record.csv', 'a',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(data)




def get_amount_of_bat():
  exit_rewards_info = (1859, 463)
  bat_amount = (1671, 462)

  hc.move((exit_rewards_info),random(0.3, 0.7))
  hc.click()
  time.sleep(0.1)
  hc.move((bat_amount),random(0.3, 0.7))   # (x=1859, y=463)
  bot.doubleClick()
  
  hotkey(['ctrl', 'c'])

  win32clipboard.OpenClipboard()
  data = win32clipboard.GetClipboardData()
  win32clipboard.CloseClipboard()
  data.split('BAT', 1)
  bat = data.split('BAT', 1)[0] 
  return bat




def turn_off_auto_contribute():
  turn_off = (1016, 872)  # Point(x=1016, y=872)   
  turn_off_2 = (1016, 843)
  learn_more = (1659, 588)

  hc.move((learn_more),random(0.2, 0.4))
  time.sleep(.4)
  hc.click()
  time.sleep(1)
  hc.move((turn_off_2),random(0.2, 0.4))
  time.sleep(.4)
  hc.click()
  time.sleep(1)
  hc.move((turn_off),random(0.2, 0.4))
  time.sleep(.4)
  hc.click()


def no_contribute(start, stop):
  close_window = (1894, 14)
  for i in range(start, stop):
    launch_as_different_user('user' + str(i))
    time.sleep(1)
    not_now_default_browser_popup()
    time.sleep(1)
    turn_off_auto_contribute()
    time.sleep(1)

    hc.move((close_window),random(1.5, 2.3))
    mouse_click()












# setup rewards wasn't always clicked
# set browser as default popup
# coraclean.cc is still loaded







# Traceback (most recent call last):
#   File "C:\Users\natha\Documents\bot\auto_gui.py", line 486, in <module>   
#     mine(master_start, master_stop, master_number_refreshes)
#   File "C:\Users\natha\Documents\bot\auto_gui.py", line 407, in mine       
#     amount_of_bat.append(get_amount_of_bat())
#   File "C:\Users\natha\Documents\bot\auto_gui.py", line 450, in get_amount_of_bat
#     data = win32clipboard.GetClipboardData()
# TypeError: Specified clipboard format is not available

# bot.MINIMUM_DURATION = 0.1
# bot.MINIMUM_SLEEP = 0.1
# bot.PAUSE = 0.1

master_url = 'https://coraclean.cc'
master_start = 54
master_stop = 151
master_monthly_contributions = True
master_auto_contribute = False
master_number_refreshes = 21

print("start")

bot.FAILSAFE_POINTS = [(0, 1079)]
# 97 ---------------------

# close_all_windows()
track_mouse()

# no_contribute(master_start, master_stop)
# create_csv()
# add_users(master_start, master_stop)  # [start, stop)
# browser_setup(master_start, master_stop)
# setup_contributions(master_start, master_stop, master_url, master_monthly_contributions, master_auto_contribute)
# mine(master_start, master_stop, master_number_refreshes)











# echo "# bot" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/natepuppy/bot.git
# git push -u origin main




