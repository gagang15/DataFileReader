import time

import pytest
from fileDataReader import DataReader
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class TestGroupModule():

    global tcId, userName, passWord, grpName, permission, x,cnt


    tcId, userName, passWord, grpName, permission, x,cnt = DataReader.readDataforgrpsave()
    # print(len(tcId))

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://mitintech.com/admin/login/?next=/admin/")
        self.driver.maximize_window()
        self.driver.find_element_by_name("username").send_keys(userName[cnt])
        self.driver.find_element_by_name("password").send_keys(passWord[cnt])
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()


        yield
        self.driver.close()

    @pytest.mark.repeat(x)
    def test_addGrpSave(self,setup):

        try:

            driver=self.driver
            driver.find_element_by_xpath('//*[@id="content-main"]/div[1]/table/tbody/tr[1]/th/a').click()
            driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
            driver.find_element_by_name("name").send_keys(grpName[0])
            per = permission[0].split(",")
            for j in per:
                driver.find_element_by_id("id_permissions_input").send_keys(j)
                select = Select(driver.find_element_by_id('id_permissions_from'))
                select.select_by_visible_text(j)
                driver.find_element_by_id("id_permissions_add_link").click()
                driver.find_element_by_id("id_permissions_input").clear()

            driver.find_element_by_name("_save").click()
            try:
                y = "login"
                if y == "login":

                    x = driver.find_element_by_xpath('//*[@id="content"]/h1').is_displayed()
                    if x=="True":
                        assert True
                    else:
                        print(x)
                        assert False

                else:
                    x = driver.find_element_by_xpath('//*[@id="content"]/h1').is_displayed()
                    print(x)
                    if x == "True":
                        assert False
                    else:
                        assert True
            except:
                assert False

        except:
            assert False



