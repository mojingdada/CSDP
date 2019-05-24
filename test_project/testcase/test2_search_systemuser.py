from selenium import webdriver
import time
import logging
import unittest
from python_selenium.test_project.testcase import readexcel
import ddt

# 输出info以上级别的日志并规定格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
excel_login = readexcel.ExcelUtil('case.xlsx', 'login')
excel_newuser = readexcel.ExcelUtil('case.xlsx', 'newuser')
excel_search = readexcel.ExcelUtil('case.xlsx', 'search')
data_login = excel_login.dict_data()
data_newuser = excel_newuser.dict_data()
data_search = excel_search.dict_data()


@ddt.ddt
class test2_search_del_systemuser(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        print("start")
        # cls.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        cls.browser = webdriver.Chrome()
        cls.html = 'http://192.168.54.124/#/login'
        cls.browser.get(cls.html)
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(30)

    # 进行清理
    @classmethod
    def tearDownClass(cls):
        logging.info("测试结束，页面即将关闭")
        time.sleep(5)
        cls.browser.quit()
        print("end")

    # 每次执行完用例进行的操作
    def tearDown(self):
        logging.info("用例执行完成，等待3秒")
        time.sleep(3)
        print(self.browser.current_url)
        # self.browser.refresh()

    @ddt.data(*data_login)
    def test1_CSDPLogin(self, data):
        u''' 测试登录用例，账号：系统管理员,密码：123456'''
        browser = self.browser
        browser.get(self.html)
        # self.username = input('Entry username:')
        # self.password = input('Entry password:')
        # 获取用户名，密码，登录键的元素位置
        self.userElement = browser.find_element_by_name("username")
        self.passwordElement = browser.find_element_by_name("password")
        self.clickElement = browser.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div/div/div[1]/form/"
                                                          "div[5]/button")
        browser.implicitly_wait(10)

        # 输入用户名，密码（用例数据）
        self.userElement.send_keys(data['username'])
        self.passwordElement.send_keys(int(data['password']))

        time.sleep(20)

    def test2_EntrySystemManage(self):
        u''' 跳转测试，进入系统管理'''
        self.systemManage = self.browser.find_element_by_xpath(
            '//*[@id="app"]/section/header/div/div[1]/div[1]/span/button').click()

    def test3_EntrySystemUserManage(self):
        u''' 跳转测试，进入系统用户管理'''
        self.systemUserManage = self.browser.find_element_by_xpath(
            '//*[@id="app"]/section/header/div/div[2]/div/ul[2]/li[3]/ul/li[2]').click()

    @ddt.data(*data_search)
    def test4_searchbyname(self, data):

        browser = self.browser
        #获取输入框
        self.searcheFiled = browser.find_element_by_xpath("//input[contains(@ng-model,'searchOptions.searchKey')]")
        self.searchbutton = browser.find_element_by_xpath("//button[contains(@class,'btn btn-primary')]")
        self.searcheFiled.send_keys(data['username'])
        self.searchbutton.click()


# 主函数
if __name__ == '__main__':
    unittest.main()
