
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.guru99.com/test/newtours/reservation.php/")
driver.maximize_window()
flight_type = driver.find_element(By.NAME, "tripType")
if flight_type.is_enabled():
    print("Road Trip")
else:
    print("One way")

passengers_num = Select(driver.find_element(By.NAME, "passCount"))
passengers_num.select_by_index(2)
passengers_num.select_by_visible_text('3')

departing_from = Select(driver.find_element(By.NAME, "fromPort"))
departing_from.select_by_index(2)
departing_from.select_by_visible_text('New York')

arrival_month = Select(driver.find_element(By.NAME, "fromMonth"))
arrival_month.select_by_index(2)
arrival_month.select_by_visible_text('August')

arrival_day = Select(driver.find_element(By.NAME, "fromDay"))
arrival_day.select_by_index(2)
arrival_day.select_by_visible_text('15')

arriving_in = Select(driver.find_element(By.NAME, "toPort"))
arriving_in.select_by_index(2)
arriving_in.select_by_visible_text('Seattle')

leaving_month = Select(driver.find_element(By.NAME, "toMonth"))
leaving_month.select_by_index(2)
leaving_month.select_by_visible_text('August')

leaving_day = Select(driver.find_element(By.NAME, "toDay"))
leaving_day.select_by_index(2)
leaving_day.select_by_visible_text('19')

airline = Select(driver.find_element(By.NAME, "airline"))
airline.select_by_index(2)
airline.select_by_visible_text('Pangea Airlines')

driver.close()

