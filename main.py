from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

PHONE = "YOURPHONE"
PASS = "YOURPASS"
chrome_driver_path = Service("/Users/israelos/Development/chromedriver")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
driver.get("https://tinder.com/app/recs")
sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div["
                              "2]/a/div[2]/div[2]").click()
sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]").click()
sleep(0.5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
driver.find_element(By.ID, "email").send_keys(EMAIL)
driver.find_element(By.ID, "pass").send_keys(PASS)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input").click()
driver.switch_to.window(base_window)
sleep(5)
driver.find_element(By.XPATH, "//*[text()='Allow']").click()
sleep(0.5)
driver.find_element(By.XPATH, "//*[text()='Not interested']").click()
driver.find_element(By.XPATH, "//*[text()='I decline']").click()
tinder = driver.find_element(By.ID, "Tinder")
for n in range(100):
    sleep(1)
    try:
        tinder.send_keys(Keys.ARROW_LEFT)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
