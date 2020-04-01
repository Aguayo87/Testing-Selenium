#Abrir un navegador y dirigirte a una url

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.coppel.com")