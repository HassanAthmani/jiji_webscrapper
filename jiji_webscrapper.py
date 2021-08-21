import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import sys
import os

class Clicker:

    def __init__(self):

        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        # chromeOptions.addArguments("--headless")
        chrome_options.add_argument("disable-gpu")

        while True:
            try:

                exePath = "C:/Users/User/Desktop/4th year/4.2/python_server/chromedriver_win32/chromedriver.exe"
                #exePath = "/usr/bin/chromedriver"
                driver = webdriver.Chrome(executable_path=exePath, options=chrome_options)
                #driver.get('https://jiji.co.ke/')
                driver.get('https://jiji.co.ke/search?query=iphone&sort=new')

                #searchbar=driver.find_element_by_css_selector("input[type='text']")#driver.find_elements_by_class_name("multiselect__input")
                #searchbar.send_keys('iphone')
                #searchbar.send_keys(Keys.ENTER)
                time.sleep(3)

                #driver.find_element_by_xpath("//li[@class='fw-menu-item qa-sort-new']")
                #adverts=driver.find_elements_by_css_selector("div.b-advert-listing js-advert-listing qa-advert-listing")
                #print(adverts)
                advert=driver.find_element_by_css_selector("div.b-list-advert__item-wrapper a").get_attribute("href")
                print(advert)



                #time.sleep()

                #time.sleep(5)

                #driver.close()
                #driver.quit()



            except selenium.common.exceptions.TimeoutException:
                driver.close()

                driver.quit()

                time.sleep(300)


Clicker()




