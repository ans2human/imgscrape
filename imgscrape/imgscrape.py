import base64
import requests
from PIL import Image
from selenium import webdriver
from urllib.request import urlopen, urlretrieve
from selenium.common.exceptions import NoSuchElementException

def imgscrape(*urls, path):
    if not urls:
        raise Exception("No url provided in argument.")
    else:
        lst = []
        for url in urls:
            driver = webdriver.Chrome(executable_path=path)
            driver.get(url)
            try:
                img_url = driver.find_element_by_id('landingImage').get_attribute('src')
            except NoSuchElementException:
                img_url = driver.find_element_by_xpath('//div[@class="_3BTv9X _3iN4zu"]/img').get_attribute('src')
            lst.append(img_url)
            driver.quit()
        return lst
    

def prod_thumbnail(img_url):
    img = Image.open(urlopen(img_url))
    return img.thumbnail((400, 400))


def image_as_base64(img_url):
    return base64.b64encode(requests.get(img_url).content)


# def savetofolder():
#     link = imgscrape()
#     filename = link.split('/')[-1]
#     img = urlretrieve(link, filename)




