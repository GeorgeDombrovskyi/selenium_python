from selenium import webdriver
import time  # For pause
from selenium.webdriver.common.by import By

from auth_data import *

# from auth_data import text_one


# link
link = "https://www.google.com/"

# Defined our Browser
browser = webdriver.Chrome()

try:
    browser.get(link)
    # Give 2 seconds pause - for give a time to document for loading
    time.sleep(2)

    # defined the web element for XPATH (in our case this is INPUT)
    our_input = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

    # clean Input Area (just in case)
    our_input.clear()

    # insert in Input Area our text, and some text from another document (auth_data.py)
    our_input.send_keys('first word + ', text_one)

    # Gave 5 seconds pause - for look our result, cause in another case window will close very quickly
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
    print('everything is OK')