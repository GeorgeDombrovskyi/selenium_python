from selenium import webdriver
import time



# link
link = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"


# Change User Agent + defined our browser
options = webdriver.ChromeOptions()
options.add_argument('user-agent=SomethingAnotherUserAgent')
browser = webdriver.Chrome(options=options)

try:
    browser.get(link)
    time.sleep(5)  # Give a 5 seconds pause
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
    print('everything is OK')