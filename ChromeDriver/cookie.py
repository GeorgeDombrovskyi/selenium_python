from selenium import webdriver
import time  # For pause
import pickle  # For save a cookie



# link
link = "https://www.google.com/"


# Defined our Browser
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Give 2 seconds pause - for give a time to document for loading
    time.sleep(1)

    # Cookies save function. Be careful .get_cookIES(), not cooKIE()
    pickle.dump(browser.get_cookies(), open("OurCookie", "wb"))

    # Gave 2 seconds pause
    time.sleep(2)

    # Get cookies from file
    for cookie in pickle.load(open(f'OurCookie', 'rb')):
        browser.add_cookie(cookie)

    # Refresh the window
    browser.refresh()

    # Gave 2 seconds pause - for look our result, cause in another case window will close very quickly
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
    print('everything is OK')
