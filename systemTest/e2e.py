from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from decouple import config


# print out the port 
TEST_SERVER_IP = config('TEST_SERVER_IP')
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

def test_heading():
    heading = driver.find_element(By.TAG_NAME,"h3")
    print("Heading value: ", heading.text)
    if heading.text == "Team 13":
        print("Pass heading testing")
    else:
        print("Failed heading testing")
        raise ValueError("Heading not correct!")

print(f"Accessing {TEST_SERVER_IP}")
driver.get(TEST_SERVER_IP)

print(driver.page_source)
test_heading()
