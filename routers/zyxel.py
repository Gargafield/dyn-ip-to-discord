import requests
from scraper import Scraper

BASE_URL = "http://{host}"

HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
}

class VMG8924(Scraper):
    def __init__(self, host=None, user=None, password=None):

        self.session = None
        self.base_url = None

        self.host = host
        self.user = user
        self.password = password

        self.connect()

    def connect(self):
        self.base_url = BASE_URL.format(host=self.host)
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.login()

    def login(self):
        try:
            response = self.session.post(self.base_url + "/login/login-page.cgi", data={"AuthName": self.user, "Display": self.password, "AuthPassword": self.password})
            
            if response.status_code != 200:
                raise Exception("Login failed")
            
            print(f"Got cookies: {self.session.cookies}")
        except Exception as e:
            raise e

    def scrape(self) -> str:
        response = self.session.get(self.base_url + "/pages/connectionStatus/GetDnsInfo.html")

        if response.status_code != 200:
            self.login()
            response = self.session.get(self.base_url + "/pages/connectionStatus/GetDnsInfo.html")

        data = response.text.split("\n")[0]
        data = data.split('|')

        index = data.index("DHCP")
        return data[index + 1]
    
    def stop(self):
        self.session.close()
