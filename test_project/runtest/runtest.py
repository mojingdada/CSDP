import unittest
from python_selenium.test_project.testcase import user_login
from python_selenium.test_project.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(user_login.CSDPTest('testCSDPLogin'))
suite.addTest(user_login.CSDPTest('testEntrySystemManage'))
suite.addTest(user_login.CSDPTest('testEntrySystemUserManage'))
suite.addTest(user_login.CSDPTest('testEntryNewUser'))
suite.addTest(user_login.CSDPTest('testNewUser'))

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    report_path = "/Users/liyulong/Documents/PycharmProjects/work/python_selenium/test_project/用例报告/html_report.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告',
                                           description=u'用例执行情况')
    runner.run(suite)
    fp.close()
