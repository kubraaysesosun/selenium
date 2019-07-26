import time
import login_info
from selenium import webdriver
import requests
from bs4 import BeautifulSoup


class TwitterPosts:
    def __init__(self):
        self.url="https://twitter.com"
        self.open_driver()

    def open_driver(self):
        driver = webdriver.Firefox()
        driver.get(self.url)
        time.sleep(3)

        login = driver.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[1]/a")
        login.click()
        time.sleep(3)

        username = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
        password = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")
        time.sleep(3)

        username.send_keys(login_info.username)
        password.send_keys(login_info.password)

        sign_in = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
        sign_in.click()
        
        driver.close()
        
if __name__ == '__main__':
    TwitterPosts()