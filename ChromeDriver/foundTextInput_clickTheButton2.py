from selenium import webdriver
import time  # For pause
from selenium.webdriver.common.by import By

from auth_data import *
# from auth_data import text_one


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# link
link = "https://www.google.com/"

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)

try:
    browser.get(link)
    # time.sleep(1)  # Give a 5 seconds pause

    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]"
                                                                                         "/form/div[1]/div[1]/div[1]/"
                                                                                         "div/div[2]/input")))

    element.clear()
    element.send_keys('first word + ', text_one)

    time.sleep(5)  # Give a 5 seconds pause

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
    print('everything is OK')