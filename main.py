# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import datetime

from selenium.webdriver.support import expected_conditions as EC

username = ""
password = ""
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.maximize_window()


def open_and_go_to_login_page(driver):
    driver.get('https://www.huji.ac.il/rooms/')
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[4]/button').click()  # login button
    frame = WebDriverWait(driver, 10)


def login_in_login_page(driver, username, password):
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/ul/li[2]/a').click()
    time.sleep(2)
    # find username/email field and send the username itself to the input field
    driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div/div[2]/form/div[1]/input").send_keys(username)
    time.sleep(2)
    # find password input field and insert password as well
    driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div/div[2]/form/div[2]/input").send_keys(password)
    time.sleep(2)
    # click login button
    driver.find_element(By.XPATH, value="/html/body/div/div/div[2]/div/div[2]/form/div[3]/button").click()
    # wait the ready state to be complete
    time.sleep(3)


def go_to_cs_rooms(driver):
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[1]/fieldset/div[7]/input').click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[3]/button').click()
    time.sleep(3)


def press_on_last_date(driver):
    all_active = driver.find_elements(by=By.CLASS_NAME, value='active')
    all_active[-1].click()
    time.sleep(5)


def fill_hours(driver):
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[3]/div[2]/div/div[2]/div[2]/div[5]').click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[4]/button[1]').click()
    time.sleep(5)


def fill_id_and_order(driver):
    #fill id in text box
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[1]/form/div[1]/input[1]').send_keys(
        '12345678')
    time.sleep(5)
    #click check id
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[1]/form/div[1]/font[1]').click()
    time.sleep(5)
    #fill id in text box
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[1]/form/div[1]/input[2]').send_keys(
        '23456789')
    time.sleep(5)
     #click check id
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[1]/form/div[1]/font[2]').click()
    time.sleep(5)
    #click hide names
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[1]/form/input[5]').click()
    time.sleep(5)
    #click finish
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[8]/div[4]/button[1]').click()
    time.sleep(5)
    #close the window and finish
    driver.close()


open_and_go_to_login_page(driver)
login_in_login_page(driver, username, password)
go_to_cs_rooms(driver)
press_on_last_date(driver)
fill_hours(driver)
fill_id_and_order(driver)

#im not sure we need it
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements(by=By.CLASS_NAME, value="flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
