from selenium import webdriver
from PIL import Image, ImageEnhance
from pytesseract import *
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
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
data_login = excel_login.dict_data()
data_newuser = excel_newuser.dict_data()


@ddt.ddt
class CSDPTest(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        print("start")
        # cls.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        cls.browser = webdriver.Chrome()
        cls.html = 'http://192.168.54.124/#/login'
        # cls.html = 'http://192.168.54.124/csdp/portal/#/manage'
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
        # while browser.current_url == 'http://192.168.54.124/#/login':
        #     verificationCode_Entry(browser, self.clickElement)
        #     try:
        #         self.error = browser.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div/div/div[1]/"
        #                                                    "form/div[6]/span")
        #         if self.error.text != "验证码错误":
        #             self.loginWarning = 1
        #         else:
        #             self.loginWarning = 0
        #     except NoSuchElementException:
        #         self.loginWarning = 0
        #     self.assertEqual(self.loginWarning, 0, msg='用户名或密码错误')
        # else:
        #     logging.info("成功登录")

    def test2_EntrySystemManage(self):
        u''' 跳转测试，进入系统管理'''
        self.systemManage = self.browser.find_element_by_xpath(
            '//*[@id="app"]/section/header/div/div[1]/div[1]/span/button').click()

    def test3_EntrySystemUserManage(self):
        u''' 跳转测试，进入系统用户管理'''
        self.systemUserManage = self.browser.find_element_by_xpath(
            '//*[@id="app"]/section/header/div/div[2]/div/ul[2]/li[3]/ul/li[2]').click()

    def test4_EntryNewUser(self):
        u''' 跳转测试，进入新建系统用户员'''
        self.newUser = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/'
                                                          'main-component/div/div/manage-component/div/div/div/'
                                                          'div[1]/div/div/div/div/div[3]/button/i').click()

    @ddt.data(*data_newuser)
    def test5_NewUser(self, data):
        u'''新建用户'''

        # 录入新建用户信息（用例数据）
        # newusername = "test1"
        # truename = '李四'
        # newpassword = "liyulong__123"
        # denewpassword = "liyulong__123"
        # email = "2015@ctsi.com.cn"
        # phone = "11111111111"
        # gudingphone = "0510-1234567"
        # QQ = "123456"
        # address = "电信集团"
        # status = "启用"
        # sex = "女"
        # 获取域输入框，用户名输入框，真实姓名输入框，新密码输入框，确认密码输入框，邮件输入框，电话输入框，QQ输入框，
        # 地址输入框和保存按键的元素位置
        self.yu = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                     'manage-component/div/div/div/div[1]/div/div[2]/'
                                                     'form/div[1]/div[1]/div/div/button[2]').click()
        self.deDomain = self.browser.find_element_by_xpath('//*[@id="9a79a677-91ad-11e6-9c77-e0db55cd9154_anchor"]'). \
            click()
        self.username = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                           'manage-component/div/div/div/div[1]/div/div[2]/form/'
                                                           'div[1]/div[2]/div/input')
        self.turename = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                           'manage-component/div/div/div/div[1]/div/div[2]/form/div[1]/'
                                                           'div[3]/div/input')
        self.newpassword = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                              'manage-component/div/div/div/div[1]/div/div[2]/form/'
                                                              'div[1]/div[4]/password-check-component/div/div/input')
        self.denewpassword = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/'
                                                                'main-component/div/div/manage-component/div/div/div/'
                                                                'div[1]/div/div[2]/form/div[1]/div[5]/div/input')
        self.email = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                        'manage-component/div/div/div/div[1]/div/div[2]/form/div[1]/'
                                                        'div[6]/div/input')
        self.phone = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                        'manage-component/div/div/div/div[1]/div/div[2]/form/div[1]/'
                                                        'div[9]/div/input')
        self.gudingphone = self.browser.find_element_by_xpath(
            '/html/body/app-component/div[1]/main-component/div/div/manage-component/div/div/div/div[1]/div/div[2]/'
            'form/div[1]/div[10]/div/input')
        self.QQ = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                     'manage-component/div/div/div/div[1]/div/div[2]/form/div[1]/'
                                                     'div[11]/div/input')
        self.address = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                          'manage-component/div/div/div/div[1]/div/div[2]/form/div[1]/'
                                                          'div[12]/div/input')
        self.sava_status = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                              'manage-component/div/div/div/div[1]/div/div[2]/form/'
                                                              'div[2]/div/div/button[1]')
        if data['status'] == "启用":
            self.item2 = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                            'manage-component/div/div/div/div[1]/div/div[2]/form/div[1]'
                                                            '/div[7]/div/div/input[1]').get_attribute('aria-owns')
            self.num2 = self.item2[-1]
            print(self.num2)
            self.statusButton = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/'
                                                                   'div/div/manage-component/div/div/div/div[1]/div/'
                                                                   'div[2]/form/div[1]/div[7]/div/div/div[1]/'
                                                                   'span/span[2]').click()
            self.statusStartup = self.browser.find_element_by_xpath(
                "//*[@id='ui-select-choices-row-" + self.num2 + "-0']/"
                                                                "span/span").click()
        elif data['status'] == "锁定":
            self.item2 = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                            'manage-component/div/div/div/div[1]/div/div[2]/form/div[1]'
                                                            '/div[7]/div/div/input[1]').get_attribute('aria-owns')
            self.num2 = self.item2[-1]
            self.statusButton = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/'
                                                                   'div/div/manage-component/div/div/div/div[1]/div/'
                                                                   'div[2]/form/div[1]/div[7]/div/div/div[1]/span/'
                                                                   'span[2]').click()
            self.statusStartup = self.browser.find_element_by_xpath(
                "//*[@id='ui-select-choices-row-" + self.num2 + "-1']/"
                                                                "span/span").click()
        else:
            logging.error("无此状态，结束测试")
            self.browser.quit()
        if data['sex'] == "男":
            self.item3 = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                            'manage-component/div/div/div/div[1]/div/div[2]/form/'
                                                            'div[1]/div[8]/div/div/input[1]').get_attribute("aria-owns")
            self.num3 = self.item3[-1]
            self.statusButton = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/'
                                                                   'div/manage-component/div/div/div/div[1]/div/div[2]/'
                                                                   'form/div[1]/div[8]/div/div/div[1]/span').click()
            self.statusStartup = self.browser.find_element_by_xpath(
                "//*[@id='ui-select-choices-row-" + self.num3 + "-1']/"
                                                                "span/span").click()
        elif data['sex'] == "女":
            self.item3 = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/div/div/'
                                                            'manage-component/div/div/div/div[1]/div/div[2]/form/'
                                                            'div[1]/div[8]/div/div/input[1]').get_attribute("aria-owns")
            self.num3 = self.item3[-1]
            self.statusButton = self.browser.find_element_by_xpath(
                '/html/body/app-component/div[1]/main-component/div/'
                'div/manage-component/div/div/div/div[1]/div/div[2]/'
                'form/div[1]/div[8]/div/div/div[1]/span').click()
            self.statusStartup = self.browser.find_element_by_xpath(
                "//*[@id='ui-select-choices-row-" + self.num3 + "-2']/"
                                                                "span/span").click()
        else:
            logging.error("无此性别，结束测试")
            self.browser.quit()

        # self.yu.click()
        # self.deDomain.click()
        self.username.send_keys(data['newusername'])
        self.turename.send_keys(data['truename'])
        self.newpassword.send_keys(data['newpassword'])
        self.denewpassword.send_keys(data['denewpassword'])
        self.email.send_keys(data['email'])
        self.phone.send_keys(int(data['phone']))
        self.gudingphone.send_keys(data['gudingphone'])
        self.QQ.send_keys(int(data['QQ']))
        self.address.send_keys(data['address'])
        # try:
        self.sava_status = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/'
                                                              'div/div/manage-component/div/div/div/div[1]/div/'
                                                              'div[2]/form/div[2]/div/div/button[1]').get_attribute(
            'disabled')

        if self.sava_status is None:
            self.save = self.browser.find_element_by_xpath('/html/body/app-component/div[1]/main-component/'
                                                           'div/div/manage-component/div/div/div/div[1]/div/'
                                                           'div[2]/form/div[2]/div/div/button[1]').click()
        else:
            logging.warning("信息输入有误")


# 输入到验证码框中
def verificationCode_Entry(browser, clickElement):
    try:
        # 获取验证码输入框
        verificationCode_field = browser.find_element_by_name("captcha")
        # 清除验证码输入框
        verificationCode_field.clear()
        # 处理验证码
        verificationCode = verificationCode_processing(browser)
        # 将验证码输入相应位置
        verificationCode_field.send_keys(verificationCode)
        # 点击登录
        clickElement.click()
    # 捕获异常，找不到对应元素即处理
    except StaleElementReferenceException:
        html1 = browser.current_url
        if html1 != "http://192.168.54.124/#/login":
            return 0
    except NoSuchElementException:
        pass


# 处理验证码，首先截网页全屏图，再通过位置截出验证码图，经过图像处理，使用tesseract识别图片信息，返回识别的验证码
def verificationCode_processing(browser):
    # 截网页全屏图
    browser.save_screenshot("../photo/01.png")
    screenImg = "../photo/01.png"
    Image.open(screenImg).crop((2100, 600, 2500, 700)).save("../photo/02.png")
    # 获取验证码图片，读取验证码
    # 图像增强，二值化
    imageCode = Image.open("../photo/02.png")
    imageCode.load()
    sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
    sharp_img.save("../photo/03.png")
    sharp_img.load()  # 对比度增强
    code = pytesseract.image_to_string("../photo/03.png").strip()
    return code


# 主函数
if __name__ == '__main__':
    unittest.main()
