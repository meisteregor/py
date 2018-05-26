# Place your login_google.txt file near this module to run your google account via Chrome browser.
# First line with email or telephone number, second - password
from selenium import webdriver
from time import sleep


def login_to_chrome():
    with open('login_google.txt', 'r') as f:
        kunteynir = list(f)

        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        log_bt_0 = driver.find_element_by_id('gb_70')
        log_bt_0.click()

        sleep(1)

        email_or_telephone = driver.find_element_by_id("identifierId")
        email_or_telephone.send_keys(kunteynir[0])
        # here is no .click method by the reason we have \n after listing .txt file

        sleep(1)

        pas = driver.find_element_by_name('password')
        pas.send_keys(kunteynir[1])
        log_bt_2 = driver.find_element_by_class_name("CwaK9")
        log_bt_2.click()


if __name__ == '__main__':
    login_to_chrome()
