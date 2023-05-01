from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.calculator.net/")
search = driver.find_element(By.ID, "calcSearchTerm")
''' 
search_button_text = search.accessible_name
if (search_button_text == "Search"):
    print("Search button text appears as expected")
'''
search.click()
search.clear()
search.send_keys("abc")
search.send_keys(Keys.ENTER)

no_exist = driver.find_element(By.ID, "calcSearchOut")

print(no_exist.text)
driver.close()
