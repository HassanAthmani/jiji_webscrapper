import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import sys
import os


def jiji():

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # chromeOptions.addArguments("--headless")
    chrome_options.add_argument("disable-gpu")

    #while True:


    exePath = "C:/Users/User/Desktop/4th year/4.2/python_server/chromedriver_win32/chromedriver.exe"
    #exePath = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(executable_path=exePath, options=chrome_options)
    #driver.get('https://jiji.co.ke/')
    driver.get('https://jiji.co.ke/search?query=iphone&sort=rel')

    #searchbar=driver.find_element_by_css_selector("input[type='text']")#driver.find_elements_by_class_name("multiselect__input")
    #searchbar.send_keys('iphone')
    #searchbar.send_keys(Keys.ENTER)
    #time.sleep(15)

    #driver.find_element_by_xpath("//li[@class='fw-menu-item qa-sort-new']")
    #adverts=driver.find_elements_by_css_selector("div.b-advert-listing js-advert-listing qa-advert-listing")
    #print(adverts)
    #advert=driver.find_element_by_css_selector(".b-list-advert__item-wrapper a").get_attribute("href")
    #adverts = driver.find_elements_by_css_selector("div.b-list-advert__wrapper.qa-advert-list-item")
    #adverts=driver.find_elements_by_xpath("//*[contains(@class,'b-list-advert__wrapper qa-advert-list-item')]")

    adverts = driver.find_elements_by_class_name("b-list-advert__wrapper")

    while len(adverts)< 20:
        driver.find_element_by_css_selector("input[type='text']").send_keys(Keys.PAGE_DOWN)
        adverts = driver.find_elements_by_class_name("b-list-advert__wrapper")
        time.sleep(1)

    #print(adverts)
    #driver.execute_script()

    time.sleep(5)
    for advert in adverts:
        #element = advert.find_element_by_xpath('//div[@class="b-list-advert__wrapper qa-advert-list-item"]/a')
        element = advert.find_elements_by_xpath("//*[contains(@class,'b-list-advert__wrapper qa-advert-list-item')]/a")
        count=0
        for el in element:
            print(el.get_attribute("href"))
            count+=1

        print(count)
        #links=advert.find_elements_by_class_name("b-list-advert__wrapper qa-advert-list-item")
        #for link in links:


        #link=advert.get_attribute("href")
        #print(link)



            #time.sleep()

            #time.sleep(5)

            #driver.close()
            #driver.quit()



jiji()




