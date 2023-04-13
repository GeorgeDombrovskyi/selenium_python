from selenium import webdriver

""" For pause function"""
import time

from selenium.webdriver.common.by import By

""" Import text from another document"""
from auth_data import *
# from auth_data import text_one

""" For waiting time for load the element."""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" For simulating keyboard Keys"""
from selenium.webdriver.common.keys import Keys


class doThis:
    """ Get arguments for our function"""
    def __init__(self, ourLink, xPath, waitingTime):
        self.link = ourLink
        self.xPath = xPath
        self.waitingTime = waitingTime

    def weTry(self):
        """ For some options for webdriver """
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(options=options)

        try:
            print(' ----- We are Started! ----- ')

            """ Open browser with link address """
            browser.get(self.link)

            """ Wait when element by the "xPath" will be loaded."""
            element = WebDriverWait(browser, self.waitingTime).until(EC.presence_of_element_located((By.XPATH, self.xPath)))

            """ Clear Input space, just in case."""
            element.clear()

            """ Insert in Input some text, and text from another document."""
            element.send_keys('first word + ', text_one)

            """ push the ENTER key on keyboard"""
            element.send_keys(Keys.ENTER)

            print('everything is OK')
            time.sleep(5)  # Give a 5 seconds pause

        except Exception as ex:
            print(ex)
            print("Not FOUND the Search input")
        finally:
            browser.close()
            browser.quit()
            print(' ----- We are Done! ----- ')


somePage = doThis("https://www.google.com/",
                  "//input[@class='gLFyf']",
                  10)


somePage2 = doThis("https://www.google.com/search"
                   "?q=xnjnj&rlz=1C5CHFA_enUA918UA"
                   "918&oq=xnjnj&aqs=chrome..69i57"
                   "j0i10i512j46i10i512j0i10i512j0i"
                   "10i30j0i10i30i625.694j0j15&source"
                   "id=chrome&ie=UTF-8",
                   "//input[@class='gLFyf']",
                    10)

somePage.weTry()
somePage2.weTry()

# //input[@class='name']
# //*[@class='name'] - for all elements (div, input, span atc)
# //*[text()='name'] - all elements where inside have exactly text "name"
# //*[contains(text(), 'name')] - all elements where inside have part of text "name". like "my name is"
# //*[contains(@class, 'name')] - all elements with atribute that  have "name". like "my name is"
# //div[@class='name'][2]//a[@class='f2'] - Inside third element div with class 'name', search link with class 'f2'
# //div[@class='name'][2]/../a[@class='f2'] - Look for third element div with class 'name', go 1 level up, search link with class 'f2'
#//a[@class='exp-r'][1]/following-sibling::a - Look for second element 'a' with class 'exp-r', get next element 'a' after our
