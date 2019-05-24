import unittest
# from python_selenium.test_project.testcase import user_login
from python_selenium.test_project.HTMLTestRunner import HTMLTestRunner
import os
# suite = unittest.TestSuite()
# suite.addTest(user_login.CSDPTest('testCSDPLogin'))
# suite.addTest(user_login.CSDPTest('testEntrySystemManage'))
# suite.addTest(user_login.CSDPTest('testEntrySystemUserManage'))
# suite.addTest(user_login.CSDPTest('testEntryNewUser'))
# suite.addTest(user_login.CSDPTest('testNewUser'))

# curpath = os.path.dirname(os.path.realpath(__file__))
curpath = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
# print(curpath)
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
case_path = os.path.join(curpath, "testcase")


def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath, pattern=rule,)
    return discover


def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    htmlreport = "/Users/liyulong/Documents/PycharmProjects/work/python_selenium/test_project/用例报告/html_report.html"
    print("测试报告生成地址：%s" % htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告',
                                           description=u'用例执行情况')
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # report_path = "/Users/liyulong/Documents/PycharmProjects/work/python_selenium/test_project/用例报告/html_report.html"
    # fp = open(report_path, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                        title=u'自动化测试报告',
    #                                        description=u'用例执行情况')
    # runner.run(suite)
    # fp.close()
    cases = add_case()
    run_case(cases)