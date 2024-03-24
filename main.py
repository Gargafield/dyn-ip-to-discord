import os
import requests
import time
from dotenv import load_dotenv
from scraper import Scraper

load_dotenv()

router_type = os.getenv("ROUTER_TYPE").lower()

router : Scraper = None

if router_type == "huawei":
    from huawei import Ax3
    router = Ax3()
elif router_type == "zyxel":
    pass # TODO

requests.post(os.getenv("WEBHOOK_URL"), json={"content": f"Starting IP address scraper for {router_type} router"})

ipaddr = None
try:
    while True:
        new_ipaddr = router.scrape()
        print(f"IP Address: {new_ipaddr}")
        if new_ipaddr != ipaddr:
            ipaddr = new_ipaddr
            requests.post(os.getenv("WEBHOOK_URL"), json={"content": f"New IP address from {router_type} router: {ipaddr}"})
        time.sleep(300) # Check every 5 minutes
except Exception as e:
    requests.post(os.getenv("WEBHOOK_URL"), json={"content": f"Error: {e}"})
finally:
    router.stop()
    requests.post(os.getenv("WEBHOOK_URL"), json={"content": f"Stopping IP address scraper for {router_type} router"})