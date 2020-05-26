import pyautogui
import webbrowser
import time

'''
Note: This only works on a fullscreen google chrome tab
'''


def open_instagram():
    try:
        webbrowser.open('https://www.instagram.com/', 1, True)
    except webbrowser.Error:
        print('error')

def login(username, password):
    x = 830
    y = 318
    time.sleep(6)
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.write(username, 0.10)
    time.sleep(1)
    pyautogui.click(830, 345)
    time.sleep(1)
    pyautogui.write(password, 0.10)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    # hopefully logins successfully wtihin 10 seconds


def dm(user):
    time.sleep(6)
    pointX = 1048
    pointY = 136
    pyautogui.click(pointX, pointY)
    time.sleep(5)
    x = 900
    y = 638
    pyautogui.click(x, y)
    time.sleep(5)
    pyautogui.write(user, 0.10)
    time.sleep(5)
    pyautogui.click(891, 434)
    # select friend button
    time.sleep(3)
    pyautogui.click(886, 326)
    # clicks the next button
    time.sleep(4)


def spam(message, repetition, delay):
    for i in range(0, repetition):
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(delay / 1000)
    print('done\n')


prompt = input('Are you already logged into Instagram?\nYes or No.\n')

if prompt.lower() == 'yes':
    message = input('Enter the message you would like to spam: ')
    user = input('Enter the instagram username you plan on messaging: ')
    repetition = int(input('Enter the number of times you want to send the message: '))
    delay = int(input('Enter the amount of time you want to wait before sending another message(in m/s): '))
    open_instagram()
    dm(user)
    spam(message, repetition, delay)
if prompt.lower() == 'no':
    username = input('Enter your instagram username: ')
    password = input('Enter your instagram password: ')
    message = input('Enter the message you would like to spam: ')
    user = input('Enter the instagram username you plan on messaging: ')
    repetition = int(input('Enter the number of times you want to send the message: '))
    delay = int(input('Enter the amount of time you want to wait before sending another message(in m/s): '))
    open_instagram()
    login(username, password)
    dm(user)
    spam(message, repetition, delay)
