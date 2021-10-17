from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

def test_heading():
    heading = driver.find_element(By.TAG_NAME,"h3")
    print("Heading values: ", heading.text)
    if heading.text != "Team 13":
        raise ValueError("Heading not correct!")

driver.get("http://13.55.209.93:7998/")

print(driver.page_source)
test_heading()
