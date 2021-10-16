from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 
from decouple import config


# print out the port 

PORT = config('PORT')

driver = webdriver.Chrome(r"./chromedriver")

def collect():
    try:
        # Place = driver.find_elements_by_class_name("tactile-searchbox-input") 

        # Place[0].clear()
        # Place[1].clear()

        # Place[0].send_keys(f"{lat1},{lon1}")
        # Place[1].send_keys(f"{lat2},{lon2}")

        # search1 = driver.find_elements_by_class_name("searchbox-searchbutton")[0]

        # search2 = driver.find_elements_by_class_name("searchbox-searchbutton")[1]
        # Place[0].send_keys(Keys.ENTER)
        # Place[1].send_keys(Keys.ENTER)

        # sleep(3)
        # Totalkilometers = driver.find_element_by_class_name( 
        #     "section-directions-trip-distance") 
        # print(Totalkilometers.text, ",")
        # return Totalkilometers.text
    
        heading = driver.find_element_by_tag_name("h3")
        print(heading.text)
    except:
        # sleep(10)
        # try:
        #     Totalkilometers = driver.find_element_by_class_name( 
        #     "section-directions-trip-distance") 
        #     print(Totalkilometers.text, ",")
        #     return Totalkilometers.text
        # except:
        #     print("0")
        #     return 0
        print("Failed to fetch")


print("Open the test server at ", PORT)
driver.get("http://54.66.27.76:7998/")
collect()

