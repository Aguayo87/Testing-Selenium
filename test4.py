#Login facebook

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
driver.get('http://www.facebook.com/')

#Colocar correo
element = driver.find_element_by_id('email')
element.send_keys(user)

#Colocar contraseña
element = driver.find_element_by_id('pass')
element.send_keys(passw)

element.send_keys(Keys.RETURN)