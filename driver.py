import os
import platform
from selenium import webdriver

def get_driver():
    driver_type = os.getenv("WEBDRIVER")
    extension = platform.system() == "Windows" and ".exe" or ""

    if driver_type == "edge":
        driver = "msedgedriver" + extension
        return webdriver.Edge(driver)
    else:
        driver = "geckodriver" + extension
        return webdriver.Firefox(driver)
