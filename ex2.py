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
search.send_keys("a")
search.send_keys(Keys.ENTER)

result = driver.find_element(By.PARTIAL_LINK_TEXT, "a")
result_button_text = result.accessible_name
print(result_button_text)

driver.close()
