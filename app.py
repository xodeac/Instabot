from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_follow_toget_follow_back():
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(5)
    elem = driver.find_element_by_name("username")
    elem_p = driver.find_element_by_name("password")
    elem.clear()
    elem.send_keys("hkbosss")
    elem_p.send_keys("khan8080")
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.get('https://www.instagram.com/explore/people/suggested/')
    time.sleep(3)
    links = driver.find_elements_by_xpath("//button[text()='Follow']")
    new = len(links)

    for link in range(new):
        content = driver.find_element_by_xpath("//a[@title]").text
        new_link = "https://www.instagram.com/"+content+"/"
        driver.get(new_link)
        time.sleep(5)
        if driver.find_element_by_class_name('BY3EC'):
            driver.find_element_by_class_name('BY3EC').click()
        else:
            driver.find_element_by_class_name('_5f5mN').click()

get_follow_toget_follow_back()