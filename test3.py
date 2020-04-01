#Login coppel

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secrets import *

#Abrir un navegador
driver = webdriver.Chrome()
#Ir a python.org
driver.get('http://www.coppel.com/')
#Click
element = driver.find_element_by_css_selector('.fw_normal').click()

#Click
element = driver.find_element_by_id('signInQuickLink').click()

driver.implicitly_wait(90) # seconds

#Colocar correo
element = driver.find_element_by_id('WC_AccountDisplay_FormInput_logonId_In_Logon_1')
element.send_keys(user)

#Colocar contraseña
element = driver.find_element_by_id('WC_AccountDisplay_FormInput_logonPassword_In_Logon_1')
element.send_keys(passw)