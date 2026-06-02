from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("http://selenium.dev")

time.sleep(3)

page_title = driver.title

print(page_title)

driver.quit()

# 4minutes
