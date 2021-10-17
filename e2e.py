# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep 
# from decouple import config


# # print out the port 
# PORT = config('PORT')

# from selenium.webdriver.chrome.options import Options

# options = Options()


# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome(options=options)

# def test_heading():
#     heading = driver.find_element_by_class_name("h3")
#     print(heading.text)
#     if heading.text != "Team 13":
#         raise ValueError("Heading not correct!")

# print("Open the test server at ", PORT)
# driver.get("http://54.66.27.76:7998/")
# test_heading()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

def test_heading():
    heading = driver.find_element_by_class_name("h3")
    print(heading.text)
    if heading.text != "Team 13":
        raise ValueError("Heading not correct!")

driver.get("http://13.55.209.93:7998/")

print(driver.page_source)
test_heading()
