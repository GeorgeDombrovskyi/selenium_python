from selenium import webdriver
import time  # For pause
import random  # For some random (random user-agent from list for example)
from fake_useragent import UserAgent  # Library for fake User Agent


# link
link = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"

user_agent_list = [
    'one-UsAg',
    'two-UsAg',
    'three-UsAg'
]



# library fake user agent. How to use (https://pypi.org/project/fake-useragent/)
# .ie  .opera  .google  .firefox  .random
useragent = UserAgent()


# Change User Agent + defined our browser
options = webdriver.ChromeOptions()

# options.add_argument("--proxy-server=138.128.91.65:8000")  # For add proxy adress

options.add_argument(f'user-agent={useragent.random}')  # For random user-agent
# options.add_argument('user-agent=SomethingAnotherUserAgent')  # For exactly user-agent
# options.add_argument(f'user-agent={random.choice(user_agent_list)}')  # For random user-agent


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