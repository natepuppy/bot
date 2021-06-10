# import pyautogui as bot
# import time
# import random as random_number
# import math
# from pyclick import HumanClicker
# import win32clipboard     # pip install pywin32
# import pandas as pd
# import csv

# hc = HumanClicker()


# def random(start, stop):
#   num = random_number.uniform(start, stop)
#   return num


# def click_picture_when_available(picture_path, wait = 0.0, recursion_depth = 0):
#     time.sleep(wait)
#     result = bot.locateCenterOnScreen(picture_path)
#     if result == None:
#         print('not found')
#         time.sleep(1.5)
#         recursion_depth += 1
#         if recursion_depth > 50:
#             return False
#         return click_picture_when_available(picture_path, recursion_depth)
#     hc.move((result[0], result[1]), random(0.1, 0.2))
#     hc.click()
#     time.sleep(wait)
#     return True


# def does_picture_exist(picture_path, wait = 0.0, recursion_depth = 0):
#     time.sleep(wait)
#     result = bot.locateCenterOnScreen(picture_path)
#     if result == None:
#         print('not found -- does_picture_exist')
#         time.sleep(0.5)
#         recursion_depth += 1
#         if recursion_depth > 2:
#             return False
#         return does_picture_exist(picture_path, recursion_depth)
#     time.sleep(wait)
#     return True


# def full_screen():
#     # hotkey(['alt', 'space', 'x'])
#     bot.keyDown('alt')
#     time.sleep(random(.1, .3))
#     bot.keyDown('space')
#     time.sleep(random(.1, .3))
#     bot.keyDown('x')
#     time.sleep(random(.1, .3))

#     bot.keyUp('alt')
#     time.sleep(random(.1, .3))
#     bot.keyUp('space')
#     time.sleep(random(.1, .3))
#     bot.keyUp('x')
#     time.sleep(random(.1, .3))


# def launch_settings():
#     user_search = "add user"
#     type_to_search = (116, 1063)

#     bot.click(type_to_search)
#     time.sleep(0.5)
#     bot.write(user_search)   
#     time.sleep(0.5)
#     bot.press('enter')
#     time.sleep(0.5)
#     full_screen()
#     time.sleep(1.0)


# def fill_out_info(index):
#     password = '0223'
#     security_question_answer = 'ans'
#     user = "user"

#     bot.write(user + str(index)) 
#     time.sleep(0.1)
#     bot.press('tab') 
#     time.sleep(0.1)
#     bot.write(password)
#     time.sleep(0.1)
#     bot.press('tab') 
#     time.sleep(0.1)
#     bot.write(password)
#     time.sleep(0.1)
#     bot.press('tab') 
#     bot.press('down') 
#     bot.press('tab') 
#     bot.write(security_question_answer)   
#     bot.press('tab') 
#     bot.press('down') 
#     bot.press('down') 
#     bot.press('tab') 
#     bot.write(security_question_answer)   
#     bot.press('tab') 
#     bot.press('down') 
#     bot.press('down') 
#     bot.press('down') 
#     bot.press('tab') 
#     bot.write(security_question_answer)   
#     bot.press('enter')  


# def add_users(start, stop):  # [start, stop)
#     exit_settings = (1893, 9) #   Point(x=1893, y=9).0
#     exit_kiosk = (3, 3) #   Point(x=1893, y=9).0

#     launch_settings()
#     bot.click(exit_settings)
#     time.sleep(2.0)

#     for i in range(start, stop):
#         launch_settings()

#         if does_picture_exist('add_user_pictures/set_up_kiosk.PNG'):
#             bot.click(exit_kiosk)

#         click_picture_when_available('add_user_pictures/add_someone_to_pc.PNG')
#         click_picture_when_available('add_user_pictures/i_dont_have_sign_in_info.PNG')
#         click_picture_when_available('add_user_pictures/add_user_without_account.PNG')
#         click_picture_when_available('add_user_pictures/user_name.PNG')

#         fill_out_info(i)
        
#         time.sleep(0.5)
#         bot.click(exit_settings)
#         time.sleep(.5)

# add_users(159, 163)




# import os
# command = 'C:\WINDOWS\system32\\net.exe user _user_2 0223 /add'
# os.system(command)






