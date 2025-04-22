from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import selenium
import platform

print(platform.architecture())


def main():
    print("Selenium version at runtime:", selenium.__version__)
    print("Selenium version:", selenium.__version__)
    print("WebDriver path:", webdriver.__file__)

    #service = Service(r"driver\chromedriver.exe")
    service = Service("C:\\Users\\lenovo\\PycharmProjects\\pythonProject\\venv_udemy_review_rolling\\driver\\chromedriver.exe")
    #options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service)
    driver.get("https://example.com")

if __name__ == "__main__":
    main()
