import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import sys
import os

class Clicker:

    def __init__(self):

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        # chromeOptions.addArguments("--headless")
        chrome_options.add_argument("disable-gpu")

        while True:
            try:
                #time.sleep(0)
                exePath = "C:/Users/User/Desktop/4th year/4.2/python_server/chromedriver_win32/chromedriver.exe"
                #exePath = "/usr/bin/chromedriver"
                driver = webdriver.Chrome(executable_path=exePath, options=chrome_options)
                driver1 = webdriver.Chrome(executable_path=exePath, options=chrome_options)
                driver.get('https://www.star-clicks.com/secure/ads.php?pid=23733163250568377')
                value = driver.find_element_by_xpath("//a").get_attribute("href")

                time.sleep(120)
                driver1.get(value)
                time.sleep(5)

                driver.close()
                driver1.close()
                driver.quit()
                driver1.quit()
                print(value)


            except selenium.common.exceptions.TimeoutException:
                driver.close()
                driver1.close()
                driver.quit()
                driver1.quit()
                time.sleep(300)
                work()

Clicker()

def work():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # chromeOptions.addArguments("--headless")
    chrome_options.add_argument("disable-gpu")

    while True:
        try:
            #time.sleep()
            exePath = "C:/Users/User/Desktop/4th year/4.2/python_server/chromedriver_win32/chromedriver.exe"
            #exePath="/usr/bin/chromedriver"
            driver = webdriver.Chrome(executable_path=exePath, options=chrome_options)
            driver1 = webdriver.Chrome(executable_path=exePath, options=chrome_options)
            driver.get('https://www.star-clicks.com/secure/ads.php?pid=23733163250568377')
            value = driver.find_element_by_xpath("//a").get_attribute("href")

            time.sleep(120)
            driver1.get(value)
            time.sleep(30)

            driver.close()
            driver1.close()
            driver.quit()
            driver1.quit()
            print(value)


        except selenium.common.exceptions.TimeoutException:
            driver.close()
            driver1.close()
            driver.quit()
            driver1.quit()
            time.sleep(300)
            Clicker()

def killer():
    p=os.getpid()
    cmd="kill -9 "+str(p)
    os.system(cmd)
