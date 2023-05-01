from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.ebay.com//")
driver.maximize_window()
search_button = driver.find_element(By.ID, "gh-btn")
search_button_text = search_button.accessible_name
if (search_button_text == "Search"):
    print("Search button text appears as expected")
driver.close()
