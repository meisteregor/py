from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from update_db import update_db
from constants import *


def up_add():
    driver = webdriver.Chrome()
    driver.get(LOGIN_PAGE)

    username = driver.find_element_by_id("username")
    username.send_keys(LOGIN)

    password = driver.find_element_by_id("password")
    password.send_keys(PASSWORD + "\n")

    driver.get(ADVERT_LINK)
    try:
        driver.get(UP_ADVERT_LINK)
        update_db(FILE_NAME_VAL)
    except NoSuchElementException:
        pass
