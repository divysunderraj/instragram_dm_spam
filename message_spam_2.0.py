from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


def login(instagram_username, instagram_password):
    browser.get('https://www.instagram.com/')
    time.sleep(1)
    username = browser.find_element_by_name('username')
    username.click()
    username.send_keys(instagram_username)
    password = browser.find_element_by_name('password')
    password.send_keys(instagram_password)
    password.send_keys(Keys.ENTER)


def setup(instagram_receiver):
    time.sleep(3)
    not_now = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
    not_now.click()

    time.sleep(1)
    go_to_dm = browser.find_element_by_class_name('xWeGp')
    go_to_dm.click()
    time.sleep(1)
    send_message = browser.find_element_by_tag_name('button')
    send_message.click()
    time.sleep(1)
    receiver = browser.find_element_by_name('queryBox')
    receiver.send_keys(instagram_receiver)
    time.sleep(1)
    select_first_option = browser.find_element_by_class_name('dCJp8')
    select_first_option.click()
    time.sleep(1)
    next_button = browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/button')
    next_button.click()
    time.sleep(1)


def spam(spam_message, repetitions):
    time.sleep(1)
    message_box = browser.find_element_by_xpath(
        '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

    for i in range(0, repetitions):
        message_box.send_keys(spam_message)
        message_box.send_keys(Keys.ENTER)

    print('done\n')



instagram_username = input('Enter your instagram username: ')
instagram_password = getpass.getpass(prompt='Enter your instagram password: ', stream=None)
instagram_receiver = input('Enter the instagram username you plan on messaging: ')
spam_message = input('Enter the message you would like to spam: ')
repetition = int(input('Enter the number of times you want to send the message: '))
browser = webdriver.Chrome('/Users/divysunderraj/Downloads/chromedriver')
login(instagram_username, instagram_password)
setup(instagram_receiver)
spam(spam_message, repetitions=repetition)
