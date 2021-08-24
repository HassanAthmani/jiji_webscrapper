from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import json


def jiji(msg_received):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-gpu")


    try:
        product=str(msg_received["product"]).replace(" ","%20")
        sort=msg_received["filter"]
        amount=msg_received["amount"]
        duration=msg_received["time"]

    except KeyError:
        return {"Error":"A key is missing"}


    exePath = "C:/Users/User/Desktop/4th year/4.2/python_server/chromedriver_win32/chromedriver.exe"
    #exePath = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(executable_path=exePath, options=chrome_options)

    #fil=""

    if sort == "recommended" or "r":
        fil ="rel"
    elif sort == "new" or "n":
        fil = "new"
    elif sort == "low price" or "l":
        fil = "price"
    elif sort == "high price" or "h":
        fil = "price_desc"
    else:
        fil = "rel"

    if not str(amount).isdigit() or int(amount)<=0:
        amount=2

    if duration == "day" or "d":
        duration="day"
    elif duration == "hour" or "h":
        duration="hour"
    elif duration == "all" or "a":
        duration=""
    else:
        duration="hour"


    driver.get('https://jiji.co.ke/search?query='+product+'&sort='+fil+'&period='+duration)


    adverts = driver.find_elements_by_class_name("b-list-advert__wrapper")


    #while len(adverts)< 20:
    q=0
    while q < 5:
        driver.find_element_by_css_selector("input[type='text']").send_keys(Keys.PAGE_DOWN)
        adverts = driver.find_elements_by_class_name("b-list-advert__wrapper")
        time.sleep(2)
        q+=1

    if len(adverts)==0:
        return {"Notification":"product not found"}


    list = []
    count = 0
    for advert in adverts:

        element = advert.find_elements_by_xpath("//*[contains(@class,'b-list-advert__wrapper qa-advert-list-item')]/a")


        for el in element:
            details = {}


            if count == int(amount):

                driver.close()
                driver.quit()
                list.append(count)
                #print(list)
                return json.dumps(list)

            elif count == len(element):

                driver.close()
                driver.quit()
                list.append(count)
                #print(list)
                return json.dumps(list)


            else:

                product=str(el.get_attribute("href"))
                driver2 = webdriver.Chrome(executable_path=exePath, options=chrome_options)
                driver2.get(product)
                time.sleep(3)

                title = str(driver2.find_element_by_xpath('//div[@class="b-advert-title-inner qa-advert-title b-advert-title-inner--h1"]').get_attribute("innerHTML")).strip()

                time_posted = str(driver2.find_element_by_xpath('//div[@class="b-advert-info-statistics h-ml-10"]/time').get_attribute("innerHTML")).strip()


                location = str(driver2.find_element_by_xpath('//div[@class="b-advert-info-statistics"]').get_attribute(
                    "innerHTML")).split("</svg>")[1].strip()

                cost = driver2.find_elements_by_xpath("//span[contains(@class,'qa-advert-price-view-value')]")
                price = ''
                for i in cost:
                    price = str(i.get_attribute("innerHTML")).strip()

                seller_name = str(driver2.find_element_by_xpath('//div[@class="b-seller-block__name"]').get_attribute("innerHTML")).strip()

                image = str(driver2.find_element_by_xpath(
                    '//picture[@class="h-flex-center h-width-100p h-height-100p h-overflow-hidden"]/source').get_attribute("srcset"))

                description = str(driver2.find_element_by_xpath('//span[@class="qa-description-text"]').get_attribute("innerHTML")).replace("\n","")

                details.update({"url":product,"title": title, "time_posted": time_posted, "location": location, "price": price,
                                "seller_name": seller_name, "image": image, "description": description})


                attributes = driver2.find_elements_by_xpath("//div[contains(@class,'b-advert-attributes-wrapper')]")

                for attribute in attributes:

                    keys=attribute.find_elements_by_xpath('//div[contains(@class,"b-advert-attribute__key")]')
                    values=attribute.find_elements_by_xpath('//div[contains(@class,"b-advert-attribute__value")]')


                    i =0
                    while i < len(keys) and len(values):

                        attribute_key=str(keys[i].get_attribute("innerHTML")).split("<")[0].strip()
                        attribute_value =str(values[i].get_attribute("innerHTML")).split("<")[0].strip()
                        details.update({attribute_key: attribute_value})
                        i+=1


                list.append(details)

                driver2.close()
                driver2.quit()
                count+=1

    list.append(count)
    #print(list)
    driver.close()
    driver.quit()



#print(jiji({"product":"iphone black","filter":"r","amount":"1"}))




