from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://shop.demoqa.com/my-account/")
driver.maximize_window()
user_name = driver.find_element(By.ID, "reg_username")
user_name.click()
user_name.clear()
user_name.send_keys("username")
email = driver.find_element(By.ID, "reg_email")
email.click()
email.clear()
email.send_keys("email")
password = driver.find_element(By.ID, "reg_password")
password.click()
password.clear()
password.send_keys("password")
register = driver.find_element(By.NAME, "register")
register_text = register.accessible_name
if (register_text == "Register"):
    print("Login button test appears as expected")
register.click()
driver.close()
