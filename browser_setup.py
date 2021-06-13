import pyautogui as bot
import time
import random as random_number
import math
from pyclick import HumanClicker
import win32clipboard     # pip install pywin32
import pandas as pd
import csv

hc = HumanClicker()

'''
open browser as a user
full screen
click skip tour
click start using rewards
exit the set as default
setup monthly contributions/ auto contribute
set cora as the place to donate
mine
track in csv
verify i am a human
'''

def close_window():
    close_window = (1894, 14)
    hc.move((close_window),random(0.05, 0.1))
    hc.click()

def close_default_browser():
    # set_as_default = (950, 255)
    not_now = (1066, 254)
    hc.move((not_now),random(0.05, 0.1))
    hc.click()

def random(start, stop):
  num = random_number.uniform(start, stop)
  return num

def full_screen():
#   bot.keyDown('alt')
#   bot.keyDown('space')
#   bot.keyDown('x')

#   bot.keyUp('alt')
#   bot.keyUp('space')
#   bot.keyUp('x')

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
  time.sleep(1)     # add moretime here to close all apps
  brave_app = (33, 31)
  run_as_different_user = (122, 132)
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
  time.sleep(2)

  full_screen()
  time.sleep(2)


def turn_off_auto_contribute():
  turn_off = (1016, 872)  # Point(x=1016, y=872)   
  turn_off_2 = (1016, 843)
  learn_more = (1659, 588)

  hc.move((learn_more),random(0.05, 0.1))
  time.sleep(.1)
  hc.click()
  time.sleep(2)
  hc.move((turn_off_2),random(0.05, 0.1))
  time.sleep(.1)
  hc.click()
  time.sleep(.1)
  hc.move((turn_off),random(0.05, 0.1))
  time.sleep(.1)
  hc.click()

def browser_setup(start, stop):
  skip_tour = (783, 658)
  start_using_rewards = (1741, 539)
  start_using_rewards_2 = (1741, 540)
  start_using_rewards_3 = (1742, 539)
  start_using_rewards_4 = (1740, 539)
  start_using_rewards_5 = (1741, 538)

  for i in range(start, stop):
    launch_as_different_user('user' + str(i))

    time.sleep(0.5)
    hc.move((skip_tour),random(0.1, 0.11))
    hc.click()

    time.sleep(1)
    close_default_browser()

    time.sleep(1)
    hc.move((start_using_rewards),random(0.05, 0.1))
    hc.click()
    time.sleep(.5)
    hc.move((start_using_rewards_2),random(0.05, 0.1))
    hc.click()
    time.sleep(.5)
    hc.move((start_using_rewards_3),random(0.05, 0.1))
    hc.click()
    time.sleep(.5)
    hc.move((start_using_rewards_4),random(0.05, 0.1))
    hc.click()
    time.sleep(.5)
    hc.move((start_using_rewards_5),random(0.05, 0.1))
    hc.click()

    time.sleep(.1)
    turn_off_auto_contribute()
    time.sleep(.5)

    close_window()


time.sleep(3)
master_start = 133
master_stop = 500
browser_setup(master_start, master_stop)



