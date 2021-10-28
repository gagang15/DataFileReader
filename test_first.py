import pytest

from selenium import webdriver
#pytest  --html=report.html --self-contained-html test_first.py #to genrate report

class TestOrangeHRM():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepageTitle(self,setup):
        print("hello")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"

    def test_login (self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangHRM"