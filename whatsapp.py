#code
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('/Users/vaishak-5510/Downloads/chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = "Friend Name"

# Replace the below string with your own message
string = "Hello friend"
y_arg = '//*[@id="side"]/div[1]/div/label/input'
input_y = wait.until(EC.presence_of_element_located((
    By.XPATH, y_arg)))
input_y.send_keys(target + Keys.ENTER)

inp_xpath = "//div[@contenteditable='true']"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(1):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)


