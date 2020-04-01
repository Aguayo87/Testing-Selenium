#Dirigirte a una url y realizar una busqueda

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Abrir un navegador
driver = webdriver.Chrome()
#Ir a python.org
driver.get('http://www.coppel.com/')
#Comprobar que el titulo de la pagina contiene la palabra python
element = driver.find_element_by_name('searchTerm')
element.send_keys('Tenis')
element.send_keys(Keys.ENTER)