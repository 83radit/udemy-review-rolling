import os
import sys
import time
import undetected_chromedriver as uc
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def resource_path(relative_path: str) -> str:
    '''
    Get absolute path to resource, works for dev and for PyInstaller
    '''
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)

print("Selenium version at runtime:", selenium.__version__)
print("Selenium version:", selenium.__version__)
print("WebDriver path:", webdriver.__file__)

if __name__=='__main__':
    wait_time = 7
    my_email = '---t@gmail.com'
    my_password = '---'

    web = 'https://www.udemy.com/'
    chromedriver_path = resource_path("driver/chromedriver.exe") # Get the latest chromedriver on https://googlechromelabs.github.io/chrome-for-testing/
    # chromedriver_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" # alternative path for windows
    chrome_service = Service(chromedriver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir=C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\User Data\\Default") # Use default user setting
    # driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver = uc.Chrome(driver_executable_path=chromedriver_path, service=chrome_service, options=chrome_options)
    driver.get(web)
    driver.maximize_window()
    input("Press ENTER to continue")
    page_num = 1 # Starting page number
    total_page = 25 # total number of page
    # while page_num <= (last_page_num):
    while page_num <= total_page :

        # Alternative links to execute
        # driver.get(f"https://www.udemy.com/home/my-courses/wishlist/?p={page_num}")
        # driver.get((f"https://www.udemy.com/home/my-courses/wishlist/?p={page_num}&sort=-enroll_time"))
        # driver.get((f"https://www.udemy.com/home/my-courses/learning/?p={page_num}&sort=-enroll_time"))
        # driver.get(f"https://www.udemy.com/user/educational-engineering-team/?p={page_num}")

        # Execute JavaScript to open the link in a new tab
        driver.execute_script(f"window.open('https://www.udemy.com/home/my-courses/learning/?p={page_num}&sort=-enroll_time', '_blank');")
        driver.switch_to.window(driver.window_handles[page_num])
        page_num += 1
        time.sleep(1)

    input("Press ENTER to continue")
    driver.quit()