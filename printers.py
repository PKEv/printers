#! python3

import requests, bs4
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='d:\PyProjects\driver\chromedriver.exe', options = options)

#------------
# Canon MF4780w
#------------
driver.get('http://192.168.3.21')
element = driver.find_elements_by_name("OK")
element[0].click()
#-------------
# status page
#-------------
title = driver.title
print(title)
statusMessage = driver.find_element_by_xpath("//*[@id='TonerInformationModule']//*[contains(@class,'StatusMessage')]")
print("Состояние катриджа: " + statusMessage.text)
#-------------
# HP LaserJet 500
#-------------
driver.get('http://192.168.3.20')
print("Открыли страницу HP LaserJet 500")
printerType = driver.find_element_by_xpath("//*[@id='brandLink']//*[contains(@class,'product')]")
cartridge1Name = driver.find_element_by_xpath("//*[@id='SupplyName0']")
cartridge2Name = driver.find_element_by_xpath("//*[@id='SupplyName1']")
cartridge3Name = driver.find_element_by_xpath("//*[@id='SupplyName2']")
cartridge4Name = driver.find_element_by_xpath("//*[@id='SupplyName3']")
cartridge5Name = driver.find_element_by_xpath("//*[@id='SupplyName4']")

cartridge1Status = driver.find_element_by_xpath("//*[@id='SupplyPLR0']")
cartridge2Status = driver.find_element_by_xpath("//*[@id='SupplyPLR1']")
cartridge3Status = driver.find_element_by_xpath("//*[@id='SupplyPLR2']")
cartridge4Status = driver.find_element_by_xpath("//*[@id='SupplyPLR3']")
cartridge5Status = driver.find_element_by_xpath("//*[@id='SupplyPLR4']")

cartridge1Type = driver.find_element_by_xpath("//*[@id='SupplyPartNumber0']")
cartridge2Type = driver.find_element_by_xpath("//*[@id='SupplyPartNumber1']")
cartridge3Type = driver.find_element_by_xpath("//*[@id='SupplyPartNumber2']")
cartridge4Type = driver.find_element_by_xpath("//*[@id='SupplyPartNumber3']")
cartridge5Type = driver.find_element_by_xpath("//*[@id='SupplyPartNumber4']")

print("Принтер " + printerType.text)
print("Картридж " + cartridge1Name.text + " полон на " + cartridge1Status.text + ",номер для заказа " + " ".join(cartridge1Type.text.split()[1:]))
print("Картридж " + cartridge2Name.text + " полон на " + cartridge2Status.text + ",номер для заказа " + " ".join(cartridge2Type.text.split()[1:]))
print("Картридж " + cartridge3Name.text + " полон на " + cartridge3Status.text + ",номер для заказа " + " ".join(cartridge3Type.text.split()[1:]))
print("Картридж " + cartridge4Name.text + " полон на " + cartridge4Status.text + ",номер для заказа " + " ".join(cartridge4Type.text.split()[1:]))
print("Картридж " + cartridge5Name.text + " полон на " + cartridge5Status.text + ",номер для заказа " + " ".join(cartridge5Type.text.split()[1:]))
#-------------
# FS-6530MFP
#-------------
driver.get('http://192.168.3.243')
try:
    element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "header_Setting")))
except:
    print("Элемент не найден")
    pass

printerType = driver.find_element_by_xpath("(//*[@id='header_Setting'])[1]")

cartridge1Name = driver.find_element_by_xpath("(//*[@id='contentrow']/tbody/tr[3]/td[1]))[4]")
cartridge1Status = driver.find_element_by_xpath("(//*[@id='contentrow']/tbody/tr[3]/td[3]))[4]")
print("Принтер " + printerType.text)
print("Картридж " + cartridge1Name.text + " полон на " + cartridge1Status.text)

driver.close()
driver.quit()
print("Конец программы")

