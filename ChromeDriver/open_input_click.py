from selenium import webdriver
import time

browser = webdriver.Chrome() 

link = "https://rozetka.com.ua/"

try:
    browser.get(link)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()