import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(3)

driver.get("https://stepik.org/lesson/25969/step/8")
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".submit-submission")

submit_button.click()
time.sleep(5)

driver.quit()
