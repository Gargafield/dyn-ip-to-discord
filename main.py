import os
import requests
import time
from dotenv import load_dotenv
from scraper import Scraper
from discord import post_webhook
from routers import get_router

load_dotenv()

router_type = os.getenv("ROUTER_TYPE").lower()
router : Scraper = get_router(router_type)

post_webhook(f"Starting IP address scraper for {router_type} router")

ipaddr = None
try:
    while True:
        new_ipaddr = router.scrape()
        print(f"IP Address: {new_ipaddr}")
        if new_ipaddr != ipaddr:
            ipaddr = new_ipaddr
            post_webhook(f"New IP address from {router_type} router: {ipaddr}")
        time.sleep(300) # Check every 5 minutes
except Exception as e:
    post_webhook(f"Error: {e}")
finally:
    router.stop()
    post_webhook(f"Stopping IP address scraper for {router_type} router")