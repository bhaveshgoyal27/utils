url = 'https://www.youtube.com/watch?v=S1T1jGLSgZ4&list=PL3oW2tjiIxvTSdJ4zqjL9dijeZ0LjcuGS'
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
r=driver.get(url)
time.sleep(15)
user_data = driver.find_elements_by_xpath('//*[@id="wc-endpoint"]')
links = []
for i in user_data:
    links.append(i.get_attribute('href'))
print("links generated")
driver.close()
driver.quit()


file1 = open("audio.txt","w")
for i in links:
    file1.write(i+"\n")
file1.close()
print("Links saved in txt file")
