__author__ = 'Denis Arkusha'

import inject
from selenium.webdriver.common.by import By
from selenium import webdriver

############# Comment these lines below before test - it is necessary to workaround #############
########### the dependency injection related auto-completion issue during tests dev.#############
#driver = webdriver.Firefox()
#element = driver.create_web_element(1)


####################            WebElements search conditions block              ####################
page_url = "http://dev7.na.crox.demandware.net/on/demandware.store/Sites-crocs_us-Site/default"
search_field = [By.NAME, "q"]
button_search = [By.CSS_SELECTOR,"html body div#wrapper div#header div#bar form#barSearch.simplesearch fieldset button"]

######################## Test Data Block ########################
text_to_search = "Test search"
text_to_search2 = "Bla bla bla"

#####################  Test PRIMITIVE Steps  #####################
@inject.param("driver","webdriver")
def open(driver):
    driver.get(page_url)

@inject.param("driver","webdriver")
def search(driver):
    element = driver.find_element(search_field)
    element.send_keys(text_to_search)

@inject.param("driver","webdriver")
def get_title(driver):
    return driver.title

@inject.param("driver","webdriver")
def get_search_result(driver):
    return driver.title