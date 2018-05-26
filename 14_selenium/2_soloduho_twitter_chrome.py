# -*- coding: utf-8 -*-
from selenium import webdriver
import logging


logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-2s [%(asctime)s]  %(message)s',
                    filename="followers.txt")


driver_chrome = webdriver.Chrome()
driver_chrome.get('https://twitter.com/solodukha')
followers_chrome = driver_chrome.find_element_by_xpath(
    "//*[@id='page-container']/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]")

soloduho_followers_chrome = followers_chrome.get_attribute('data-count')
logging.info('Alexander Solodukho has {} followers in twitter.'.format(soloduho_followers_chrome))