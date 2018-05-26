# IDs of searching boxes were previously prepared to gather info in dictionary
from selenium import webdriver

searching_phrase = 'Aleksandr Soloduha\n'
driver_chrome = webdriver.Chrome()
dict_of_sites_to_search = {'https://www.yahoo.com': 'uh-search-box',
                           'https://www.google.com': 'lst-ib',
                           'https://banana.by': 'searchinput',
                           'https://www.tut.by': 'search_from_str'}


def start_to_search():
    for key in dict_of_sites_to_search:
        driver_chrome.get(key)
        search = driver_chrome.find_element_by_id(dict_of_sites_to_search[key])
        search.send_keys(searching_phrase)


if __name__ == '__main__':
    start_to_search()
