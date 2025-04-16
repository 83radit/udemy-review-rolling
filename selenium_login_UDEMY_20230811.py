from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc

if __name__=='__main__':
    wait_time = 7
    my_email = '---t@gmail.com'
    my_password = '---'

    web = 'https://www.udemy.com/'
    # web = 'https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F'
    chromedriver_path = "./chromedriver/chromedriver.exe" # Get the latest chromedriver on https://googlechromelabs.github.io/chrome-for-testing/
    chrome_service = Service(chromedriver_path)
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # chrome_options.add_argument('--enable-cookies')
    # chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"')
    # chrome_options.add_argument('--proxy-server="http://127.0.0.1:8080"')
    chrome_options.add_argument("--user-data-dir=C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    driver = uc.Chrome(driver_executable_path=chromedriver_path, service=chrome_service, options=chrome_options)
    # capabilities = webdriver.DesiredCapabilities.CHROME
    # capabilities['userAgent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    # print(capabilities['userAgent'])
    driver.get(web)
    # driver.implicitly_wait(3)
    driver.maximize_window()
    input("Press ENTER to continue")
    # time.sleep(wait_time)
    # login_link = driver.find_element(By.XPATH, "//a[@data-purpose='header-login']")
    # login_link.click()
    # time.sleep(wait_time)
    # input("Press ENTER to continue")
    # driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(my_email)
    # driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(my_password)
    # input("Press ENTER to continue")
    # submit_button = driver.find_element(By.CSS_SELECTOR, "#udemy > div.ud-main-content-wrapper > div.ud-main-content > div > div > form > button")
    # submit_button.click()
    # time.sleep(wait_time)
    # # input("Press ENTER to continue")
    # wishlist_button = driver.find_element(By.XPATH, '//a[@data-purpose="wishlist-icon"]')
    # wishlist_button.click()
    # time.sleep(wait_time)
    # last_page = driver.find_element(By.CSS_SELECTOR, "#tabs--1-content-2 > div > nav > a:nth-child(6)")
    # last_page_num = int(last_page.text)
    page_num = 1 # Starting page number
    total_page = 20 # total number of page
    # while page_num <= (last_page_num):
    while page_num <= total_page :
        # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
        # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.NUMPAD2)
        driver.execute_script("window.open('', '_blank');")
        # input("Press ENTER to continue")
        # print(f'len(driver.window_handles): {len(driver.window_handles)}')
        driver.switch_to.window(driver.window_handles[page_num])
        # driver.get(f"https://www.udemy.com/home/my-courses/wishlist/?p={page_num}")
        # driver.get((f"https://www.udemy.com/home/my-courses/wishlist/?p={page_num}&sort=-enroll_time"))
        driver.get((f"https://www.udemy.com/home/my-courses/learning/?p={page_num}&sort=-enroll_time"))
        page_num += 1
        time.sleep(1)

    input("Press ENTER to continue")
    driver.quit()
