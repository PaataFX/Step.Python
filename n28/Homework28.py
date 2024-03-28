import requests
import threading
import time

def get_website_status(website):
    while True:
        response = requests.get(website)
        print(f"Website: {website}, Status Code: {response.status_code}")
        time.sleep(10)

websites = ["https://www.example1.com", "https://www.example2.com", "https://www.example3.com"]

threads = []

for website in websites:
    thread = threading.Thread(target=get_website_status, args=(website,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
