import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from fileDataReader import DataReader


driver = webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\\chromedriver.exe")
driver.get("http://mitintech.com/admin/login/?next=/admin/")
driver.maximize_window()
tcId,userName,passWord,grpName,permission = DataReader.readDataforgrpsave()
try:
    driver.find_element_by_name("username").send_keys(userName[0])
    driver.find_element_by_name("password").send_keys(passWord[0])
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
finally:
    try:
        driver.find_element_by_xpath('//*[@id="content-main"]/div[1]/table/tbody/tr[1]/th/a').click()
        driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
        for i in range(len(tcId)):
            driver.find_element_by_name("name").send_keys(grpName[i])
            permission=permission[i].split(",")
            for j in permission:
                driver.find_element_by_id("id_permissions_input").send_keys(j)
                select = Select(driver.find_element_by_id('id_permissions_from'))
                select.select_by_visible_text(j)
                driver.find_element_by_id("id_permissions_add_link").click()
                driver.find_element_by_id("id_permissions_input").clear()

        time.sleep(5)
        driver.find_element_by_name("_save").click()

    except:
        print("error")
