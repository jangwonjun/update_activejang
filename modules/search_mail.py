from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from env import MAILACCOUNT
from time import *

class at_send_mail:
    
    def __init__(self):
        
        browser = webdriver.Chrome(ChromeDriverManager().install())

        browser.get("http://webmail.activejang.com/")  

        sleep(2)
        browser.find_element(By.ID,"rcmloginuser").send_keys(MAILACCOUNT.ID)
        sleep(2)
        browser.find_element(By.ID,"rcmloginpwd").send_keys(MAILACCOUNT.PASSWORD)
        sleep(3)
        browser.find_element(By.ID,"rcmloginsubmit").click()
        print("successfully login")
        sleep(1)

        browser.quit()
