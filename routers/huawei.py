# https://github.com/krlsedu/huawei-metrics/blob/master/services/Huawei.py

import os
import requests
import time

from scraper import Scraper
from driver import get_driver

BASE_URL = "http://{host}"

HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
}

class Ax3(Scraper):
    def __init__(self, host=None, user=None, password=None):

        self.browser = None
        self.base_url = None

        if host is None:
            host = os.getenv('HUAWEI_HOST')
        self.host = host

        if user is None:
            user = os.getenv('HUAWEI_USER')
        self.user = user

        if password is None:
            password = os.getenv('HUAWEI_PASSWORD')
        self.password = password

        self.connect()

    def connect(self):
        self.base_url = BASE_URL.format(host=self.host)
        self.browser = get_driver()
        self.login()

    def login(self):
        try:
            self.browser.get(self.base_url + "/html/index.html#/login")
            self.browser.implicitly_wait(2) # Wait for the page to load

            elem = self.browser.find_element_by_id("userpassword_ctrl")
            elem.clear()
            elem.send_keys(self.password)

            elem = self.browser.find_element_by_id("loginbtn")
            elem.click()
            self.browser.implicitly_wait(2) # Wait for the page to load
            time.sleep(2)
        except Exception as e:
            raise e

    def scrape(self) -> str:
        time.sleep(2) # Wait for cookies to load
        cookie = self.browser.get_cookie("SessionID_R3")
        response = requests.get(self.base_url + "/api/ntwk/wan?type=active", cookies={"SessionID_R3": cookie['value']}, headers=HEADERS)

        if response.status_code == 404:
            self.login()
            cookie = self.browser.get_cookie("SessionID_R3")
            response = requests.get(self.base_url + "/api/ntwk/wan?type=active", cookies={"SessionID_R3": cookie['value']}, headers=HEADERS)

        data = response.json()
        return data['IPv4Addr']
    
    def stop(self):
        self.browser.quit()
